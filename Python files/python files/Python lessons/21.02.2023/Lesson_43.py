import sqlite3 as sq

with sq.connect('db_3.db') as con:
    cur = con.cursor()
    cur.execute('''
    SELECT *
    FROM T1
    ORDER BY Fname
    LIMIT 5 OFFSET 2
     ''')

    res = cur.fetchmany(3)
    print(res)

    # res = cur.fetchone()
    # print(res)

    # res = cur.fetchall()
    # print(res)

    # for res in cur:
    #     print(res)
    print(2131)