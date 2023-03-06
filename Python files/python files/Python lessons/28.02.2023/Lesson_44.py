import sqlite3 as sq

# cars = [
#     ('Mercedes', 12005),
#     ('Citroen', 132423),
#     ('Honda', 124453),
#     ('Toyota', 144534),
#     ('KIA', 11565)
# ]
#
# with sq.connect('cars.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#      ''')
#
#     cur.executescript("""
#       DELETE FROM cars WHERE model LIKE 'C%';
#       UPDATE cars SET price = price + 100;
#      """)

# cur.execute('UPDATE cars SET price=:Price WHERE model LIKE "B%"', {'Price':0})

# cur.executemany("INSERT INTO cars VALUES(NULL,?,?)", cars)

# for car in cars:
#     cur.execute("INSERT INTO cars VALUES(NULL,?,?)", car)


# cur.execute('INSERT INTO cars VALUES(1,"Renaut", 2000)')
# cur.execute('INSERT INTO cars VALUES(2,"BMW", 1000)')
# cur.execute('INSERT INTO cars VALUES(3,"Volvo", 3000)')
# cur.execute('INSERT INTO cars VALUES(4,"Audi", 4000)')
# cur.execute('INSERT INTO cars VALUES(5,"Lada", 900)')

# con = None
# try:
#     con = sq.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL,"Renaut", 2000);
#     UPDATE cars SET price = price + 100;
#      ''')
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print(f'Ошибка выполнения запроса {e}')
# finally:
#     if con:
#         con.close()


# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#      ''')

# cur.execute('SELECT model, price FROM cars')
# rows = cur.fetchall()
# rows = cur.fetchone()
# rows = cur.fetchmany(5)
# print(rows)

# for res in cur:
#     print(res)

# for res in cur:
#    print(res['model'], res['price'])

# def read_ava(n):
#     try:
#         with open(f'avatars/{n}.png', 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ava BLOB
#     );
#      ''')
#     img = read_ava(1)
#     if img:
#         binary = sq.Binary(img)
#         cur.execute("INSERT INTO users VALUES (?,?)", (1, binary))

with sq.connect('cars.db') as con:
    cur = con.cursor()
    # with open('sql_dump.sql', 'w') as f:
    #     for sql in con.iterdump():
    #         f.write(sql)
    with open('sql_dump.sql', 'r') as f:
        sql = f.read()
        cur.executescript(sql)