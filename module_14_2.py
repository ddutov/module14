"""
Для решения этой задачи вам понадобится решение предыдущей.
Для решения необходимо дополнить существующий код:
Удалите из базы данных not_telegram.db запись с id = 6.
Подсчитать общее количество записей.
Посчитать сумму всех балансов.
Вывести в консоль средний баланс всех пользователя.
"""
import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('DELETE FROM Users')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(10):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i + 1}', f'example{i +1}@gmail.com', f'{(i + 1) * 10}', '1000'))

cursor.execute('UPDATE Users SET balance = ? WHERE id%2 != 0', ('500',))
cursor.execute('DELETE FROM Users WHERE (id+2)%3 = 0')
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', ('60',))
users = cursor.fetchall()
for user in users:
    print(user)
cursor.execute('DELETE FROM Users WHERE id = 6')
cursor.execute('SELECT COUNT(*) FROM Users')
count_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
total_balances = cursor.fetchone()[0]
cursor.execute('SELECT AVG(balance) FROM Users')
average_balance = cursor.fetchone()[0]
print(f'Всего пользователей: {count_users}')
print(f'Суммарный баланс пользователей: {total_balances}')
print(f'Средний баланс: {average_balance}')

connection.commit()
connection.close()
