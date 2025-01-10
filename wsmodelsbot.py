import logging
import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv
import json
from db_manager import DBManager
from nlp_processor import NLPProcessor
from content_moderator import ContentModerator

# Configuración básica
load_dotenv(dotenv_path='bot_token.env')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load bot token from environment variable
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("Bot token not found. Please set TELEGRAM_BOT_TOKEN in your bot_token.env file.")
    raise ValueError("No TELEGRAM_BOT_TOKEN found in bot_token.env file. Please add your Telegram bot token.")

# Create the Application instance
application = Application.builder().token(BOT_TOKEN).build()

# Inicializar componentes
db_manager = DBManager()
nlp_processor = NLPProcessor()
content_moderator = ContentModerator()

# Estructuras de datos
with open('dialogos.json', 'r', encoding='utf-8') as f:
    DIALOGOS = json.load(f)

with open('imagenes.json', 'r', encoding='utf-8') as f:
    IMAGENES = json.load(f)

# Define command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Asian", callback_data='personaje_asian'),
         InlineKeyboardButton("Blondie", callback_data='personaje_blondie')],
        [InlineKeyboardButton("Italian", callback_data='personaje_italian')],
        [InlineKeyboardButton("Ebony", callback_data='personaje_ebony'),
         InlineKeyboardButton("Latina", callback_data='personaje_latina')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('¡Bienvenido! Elige un personaje:', reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    personaje = query.data.split('_')[1]
    context.user_data['personaje'] = personaje
    context.user_data['estado'] = 'inicio'
    
    await query.edit_message_text(f"Has seleccionado a {personaje.capitalize()}")
    await send_dialog(query, context, personaje, 'inicio')

async def send_dialog(query, context: ContextTypes.DEFAULT_TYPE, personaje: str, estado: str) -> None:
    try:
        if personaje not in DIALOGOS:
            raise ValueError(f"Personaje '{personaje}' no encontrado en dialogos.json")
        if estado not in DIALOGOS[personaje]['estados']:
            raise ValueError(f"Estado '{estado}' no encontrado para el personaje '{personaje}' en dialogos.json")

        dialogo = DIALOGOS[personaje]['estados'][estado][0]
        texto = dialogo['texto']
        opciones = dialogo['opciones']
        
        keyboard = [[InlineKeyboardButton(opcion[0], callback_data=f"{personaje}_{opcion[1]}")] for opcion in opciones]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.reply_text(texto, reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error in send_dialog: {str(e)}")
        await query.message.reply_text(f"Ocurrió un error al procesar el diálogo: {str(e)}")

async def handle_option(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data.split('_')
    personaje = data[0]
    estado = data[1]
    
    context.user_data['estado'] = estado
    await send_dialog(query, context, personaje, estado)

async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE, personaje: str, estado: str) -> None:
    try:
        image_folder = 'imagenes'
        image_files = [f for f in IMAGENES[personaje][estado]]
        if not image_files:
            raise ValueError(f"No images found for {personaje}/{estado}")

        image_path = os.path.join(image_folder, random.choice(image_files))
        await update.message.reply_photo(photo=open(image_path, 'rb'))
    except Exception as e:
        logger.error(f"Error in send_image: {str(e)}")
        await update.message.reply_text(f"Ocurrió un error al procesar la imagen: {str(e)}")

# Add handlers to the application
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button_callback, pattern='^personaje_'))
application.add_handler(CallbackQueryHandler(handle_option, pattern='^[a-z]+_[a-z]+$'))

# Start the bot
if __name__ == "__main__":
    try:
        logger.info("Starting bot...")
        application.run_polling()
    except Exception as e:
        logger.error(f"Error al iniciar el bot: {e}")

