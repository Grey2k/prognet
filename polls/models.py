from utils import select


class Profile:
    @staticmethod
    async def get_by_user_id(conn, user_id):
        profiles = await select(
            conn, "SELECT * FROM profiles WHERE user_id=%s", int(user_id))
        if profiles:
            return profiles[0]
        return None


    @staticmethod
    async def get_all_names(conn):
        q = "SELECT first_name, last_name, user_id FROM profiles LIMIT 100;"
        return await select(conn, q)


    @staticmethod
    async def save(conn, data):
        statement = """
            INSERT INTO profiles 
                (user_id, first_name, last_name, sex, interests, city, date_of_birth) 
            values 
                (%(user_id)s, %(first_name)s, %(last_name)s, %(sex)s, %(interests)s, %(city)s, %(date_of_birth)s)
            ON DUPLICATE KEY UPDATE
                user_id=%(user_id)s, first_name=%(first_name)s, last_name=%(last_name)s,
                sex=%(sex)s, interests=%(interests)s, city=%(city)s, date_of_birth=%(date_of_birth)s;
            """

        async with conn.cursor() as cur:
            await cur.execute(
                statement, args=dict(
                    user_id=data['user_id'], first_name=data['first_name'],
                    last_name=data['last_name'], sex=data['gender'],
                    interests=data['interests'], city=data['city'], date_of_birth=data['birth']))

    @staticmethod
    async def search(conn, params):
        for key, val in params.items():
            params[key] = f'{val}%'

        query = "SELECT * FROM profiles where first_name like %(first_name)s and last_name like %(last_name)s ORDER BY id"
        return await select(conn, query, dict(params))


class Post:
    @staticmethod
    async def save(conn, data):
        sql = """INSERT INTO posts (author_id, `text`, `datetime`) values (%(author_id)s, %(text)s, NOW());"""
        async with conn.cursor() as cur:
            await cur.execute(
                sql, args=dict(author_id=data['author_id'], text=data['text']))


    @staticmethod
    async def get_by_author_id(conn, author_id):
        posts = await select(conn, "SELECT * from posts where author_id = %s order by `datetime` desc", author_id)
        return posts
