class ContentModerator:
    def __init__(self):
        self.banned_words = ['palabrota1', 'palabrota2', 'palabrota3']  # Añade palabras prohibidas aquí

    def is_appropriate(self, text):
        return all(word.lower() not in text.lower() for word in self.banned_words)

# Removed invalid JSON block
{
    "asian": {
        "nombre": "Miyu",
        "estados": {
            "inicio": [
                {
                    "texto": "Hola, soy Miyu! 😊 ¿Te gustaría charlar un rato?",
                    "opciones": [
                        ["Claro, me encantaría", "chat"],
                        ["¿Qué tal si vamos a cenar?", "dinner"],
                        ["Preferiría dar un paseo", "walk"]
                    ]
                }
            ],
            "coqueteo": [
                {
                    "texto": "Me encanta tu compañía... ¿Qué te gustaría hacer ahora?",
                    "opciones": [
                        ["Bailar contigo", "dance"],
                        ["Tomar algo juntos", "drink"],
                        ["Ir a un lugar más privado", "private"]
                    ]
                }
            ],
            "intimo": [
                {
                    "texto": "Estoy muy emocionada... ¿Qué te gustaría hacer?",
                    "opciones": [
                        ["Seguir hablando", "talk"],
                        ["Comprar contenido especial", "buy"],
                        ["Volver al inicio", "restart"]
                    ]
                }
            ]
        }
    },
    "blondie": {
        "nombre": "Blondie",
        "estados": {
            "inicio": [
                {
                    "texto": "¡Hola! Soy Blondie. ¿Qué te apetece hacer?",
                    "opciones": [
                        ["Charlar un rato", "chat"],
                        ["Ir a cenar", "dinner"],
                        ["Dar un paseo", "walk"]
                    ]
                }
            ],
            "coqueteo": [
                {
                    "texto": "Me fascina tu presencia... ¿Qué planes tienes en mente?",
                    "opciones": [
                        ["Bailar juntos", "dance"],
                        ["Tomar una copa", "drink"],
                        ["Buscar un sitio más íntimo", "private"]
                    ]
                }
            ],
            "intimo": [
                {
                    "texto": "Estoy muy excitada... ¿Qué deseas hacer ahora?",
                    "opciones": [
                        ["Seguir conversando", "talk"],
                        ["Adquirir contenido exclusivo", "buy"],
                        ["Volver al principio", "restart"]
                    ]
                }
            ]
        }
    },
    "italian": {
        "nombre": "Giulia",
        "estados": {
            "inicio": [
                {
                    "texto": "Ciao, sono Giulia! ¿Qué te gustaría hacer?",
                    "opciones": [
                        ["Charlar un poco", "chat"],
                        ["Ir a cenar", "dinner"],
                        ["Pasear juntos", "walk"]
                    ]
                }
            ],
            "coqueteo": [
                {
                    "texto": "Me encanta estar contigo... ¿Qué te apetece hacer ahora?",
                    "opciones": [
                        ["Bailar", "dance"],
                        ["Tomar algo", "drink"],
                        ["Buscar un lugar más privado", "private"]
                    ]
                }
            ],
            "intimo": [
                {
                    "texto": "Estoy muy excitada... ¿Qué te gustaría hacer?",
                    "opciones": [
                        ["Seguir hablando", "talk"],
                        ["Comprar contenido especial", "buy"],
                        ["Volver al inicio", "restart"]
                    ]
                }
            ]
        }
    },
    "ebony": {
        "nombre": "Amara",
        "estados": {
            "inicio": [
                {
                    "texto": "¡Hola! Soy Amara. ¿Qué te gustaría hacer?",
                    "opciones": [
                        ["Charlar un rato", "chat"],
                        ["Ir a cenar", "dinner"],
                        ["Dar un paseo", "walk"]
                    ]
                }
            ],
            "coqueteo": [
                {
                    "texto": "Me encanta tu compañía... ¿Qué planes tienes?",
                    "opciones": [
                        ["Bailar juntos", "dance"],
                        ["Tomar algo", "drink"],
                        ["Buscar un lugar más íntimo", "private"]
                    ]
                }
            ],
            "intimo": [
                {
                    "texto": "Estoy muy emocionada... ¿Qué te gustaría hacer ahora?",
                    "opciones": [
                        ["Seguir conversando", "talk"],
                        ["Comprar contenido exclusivo", "buy"],
                        ["Volver al inicio", "restart"]
                    ]
                }
            ]
        }
    },
    "latina": {
        "nombre": "Camila",
        "estados": {
            "inicio": [
                {
                    "texto": "¡Hola! Soy Camila. ¿Qué te apetece hacer?",
                    "opciones": [
                        ["Charlar un poco", "chat"],
                        ["Ir a cenar", "dinner"],
                        ["Dar un paseo", "walk"]
                    ]
                }
            ],
            "coqueteo": [
                {
                    "texto": "Me encanta estar contigo... ¿Qué te gustaría hacer ahora?",
                    "opciones": [
                        ["Bailar", "dance"],
                        ["Tomar algo", "drink"],
                        ["Buscar un lugar más privado", "private"]
                    ]
                }
            ],
            "intimo": [
                {
                    "texto": "Estoy muy excitada... ¿Qué deseas hacer?",
                    "opciones": [
                        ["Seguir hablando", "talk"],
                        ["Comprar contenido especial", "buy"],
                        ["Volver al inicio", "restart"]
                    ]
                }
            ]
        }
    }
}

