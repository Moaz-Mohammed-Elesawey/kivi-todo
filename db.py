import sqlite3


class DataBase:
    __tablename__ = 'todos'
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cur = self.conn.cursor()

        self.cur.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.__tablename__} (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NULL,
                created_at TEXT NOT NULL,
                expire_at TEXT NOT NULL,
                done INT NOT NULL
            );
        ''')
        self.conn.commit()

    def fetch(self):
        self.cur.execute(f'''
            SELECT * FROM {self.__tablename__};
        ''')
        _todos = self.cur.fetchall()
        return _todos

    def fetch_one(self, id):
        self.cur.execute(f'''
            SELECT * FROM {self.__tablename__} WHERE id=?;
        ''', (id,))
        _todo = self.cur.fetchone()
        return _todo

    def insert(self, title, desc, created_at, expire_at, done=0):
        self.cur.execute(f'''
            INSERT INTO {self.__tablename__} VALUES (
                NULL,
                ?,
                ?,
                ?,
                ?,
                ?
            );
        ''', (title, desc, created_at, expire_at, done))
        self.conn.commit()

    def update(self, id, title, desc):
        self.cur.execute(f'''
            UPDATE {self.__tablename__} SET
            title=?,
            description=?
            WHERE id=?
        ''', (title, desc, id))
        self.conn.commit()

    def update_status(self, id):
        self.cur.execute(f'''
            UPDATE {self.__tablename__} SET
            done={1}
            WHERE id=?
        ''', (id,))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute(f'''
            DELETE FROM {self.__tablename__} WHERE id=?
        ''', (id,))
        self.conn.commit()

    def remove_all(self):
        self.cur.execute(f'''
            DELETE FROM {self.__tablename__}
        ''')
        self.conn.commit()

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    db = DataBase()
    db.insert('title', 'description', 'created_at', 'expire_at')
    print(db.fetch())
    db.update(1, 'update title', 'update desc')
    print(db.fetch())
    db.update_status(1)
    print(db.fetch())
    db.remove(1)
    print(db.fetch())
    db.remove_all()
    print(db.fetch())
