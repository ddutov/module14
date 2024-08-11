import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()


# cursor.execute('DELETE FROM Products')

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )
    ''')


def get_all_products(id):
    current_product = cursor.execute('SELECT * FROM Products WHERE id = ?', (id,)).fetchall()[0]
    connection.commit()
    return current_product



initiate_db()

# for i in range(1, 5):
#     cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
#                    (f'Продукт {i}', f'Описание {i}', f'{(i) * 100}'))


connection.commit()
