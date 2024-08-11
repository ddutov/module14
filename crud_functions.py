import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()
connection2 = sqlite3.connect('users.db')
cursor2 = connection2.cursor()


# cursor.execute('DELETE FROM Products')
# cursor.execute('DELETE FROM Users')

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )
    ''')
    connection.commit()
    cursor2.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age TEXT NOT NULL,
    balance INTEGER
    )
    ''')
    connection2.commit()


def get_all_products(id):
    current_product = cursor.execute('SELECT * FROM Products WHERE id = ?', (id,)).fetchall()[0]
    connection.commit()
    return current_product


def add_user(username, email, age):
    print(username, email, age)
    cursor2.execute('INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
                    (username, email, age, '1000'))
    connection2.commit()


def is_include(username):
    check = cursor2.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check.fetchone() is None:
        return True
    return False


initiate_db()

# for i in range(1, 5):
#     cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
#                    (f'Продукт {i}', f'Описание {i}', f'{(i) * 100}'))


connection.commit()
connection2.commit()
# connection.close()
