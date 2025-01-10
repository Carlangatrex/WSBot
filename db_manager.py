import aiosqlite

class DBManager:
    def __init__(self):
        self.db_name = 'bot_database.db'

    async def init_db(self):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS user_states (
                    user_id INTEGER PRIMARY KEY,
                    personaje TEXT,
                    estado TEXT,
                    items_comprados TEXT
                )
            ''')
            await db.commit()

    async def get_user_state(self, user_id):
        async with aiosqlite.connect(self.db_name) as db:
            async with db.execute('SELECT * FROM user_states WHERE user_id = ?', (user_id,)) as cursor:
                row = await cursor.fetchone()
                if row:
                    return {
                        'personaje': row[1],
                        'estado': row[2],
                        'items_comprados': row[3].split(',') if row[3] else []
                    }
                return None

    async def set_user_state(self, user_id, state):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute('''
                INSERT OR REPLACE INTO user_states (user_id, personaje, estado, items_comprados)
                VALUES (?, ?, ?, ?)
            ''', (user_id, state['personaje'], state['estado'], ','.join(state.get('items_comprados', []))))
            await db.commit()

    async def update_user_state(self, user_id, updates):
        current_state = await self.get_user_state(user_id)
        if current_state:
            current_state.update(updates)
            await self.set_user_state(user_id, current_state)

    async def add_purchased_item(self, user_id, item):
        current_state = await self.get_user_state(user_id)
        if current_state:
            items = current_state.get('items_comprados', [])
            items.append(item)
            current_state['items_comprados'] = items
            await self.set_user_state(user_id, current_state)

