import sqlite3


class HeaderDB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = 'SELECT * FROM menu'
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения из Базы данных')
        return []

    def add_admin_card(self, images, name, title, price):
        try:
            self.__cur.execute('SELECT COUNT() as "count" FROM cards WHERE name LIKE ?', (name, ))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print(f'Товар {name} уже существует')
                return False

            self.__cur.execute("INSERT INTO cards VALUES(NULL, ?, ?, ?, ?)", (images, name, title, price))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавление товара в БД:', e)
            return False
        return True








    def get_card_anons(self):
        try:
            self.__cur.execute('SELECT id, images, name, title, price FROM cards')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получение товара из БД', e)
        return []

