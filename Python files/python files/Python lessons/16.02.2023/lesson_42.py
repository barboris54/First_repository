import sqlite3 as sq

with sq.connect('user.db') as con:
    cur = con.cursor()
    cur.execute('''
    DROP TABLE person_table
     ''')

    # cur.execute('''
    #     ALTER TABLE person_table
    #     DROP COLUMN Home_adress
    #      ''')


    # cur.execute('''
    # ALTER TABLE person_table
    # RENAME COLUMN address TO Home_adress
    #  ''')


    # cur.execute('''
    # # ALTER TABLE person_table
    # # ADD COLUMN address TEXT NOT NULL
    # # ''')

    # cur.execute('''
    # ALTER TABLE person
    # RENAME TO person_table;
    # ''')


    # cur.execute('''CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT '+79099000000',
    # age INTEGER NOT NULL CHECK(age>15 AND age<70),
    # email TEXT UNIQUE
    #
    # )''')