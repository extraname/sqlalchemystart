import sqlite3

conn = sqlite3.connect('untitled.db')

# with conn:
#     conn.execute('''insert into users(username, email, password, age,
#     city) values("Katarina", "kata@gmail.com", "12343", 18, "Nikolaev")''')
#     conn.execute('''insert into users(username, email, password, age,
#     city) values('Kate', 'kate@yandex.com', '123422112', 27, 'Berdyansk')''')
#     conn.execute('''insert into users(username, email, password, age,
#     city) values('Don', 'don@gmail.com', '32167', 12, 'Chicago')''')

# with conn:
#     curs = conn.cursor()
#     curs.execute('select username, city, email, age, city from users')
#     print(curs.fetchall())

with conn:
    curs = conn.cursor()
    curs.execute('select * from USERS')
    print(curs.fetchall())

# with conn:
#     curs = conn.cursor()
#     curs.execute('''select * from users where city = "Berdyansk"''')
#     print(curs.fetchall())
#
# with conn:
#     curs = conn.cursor()
#     curs.execute('''select * from users where city = "Berdyansk" or age >
#     27''')
#     print(curs.fetchall())
#
# with conn:
#     curs = conn.cursor()
#     curs.execute('''select * from users where age between 20 and 30 ''')
#     print(curs.fetchall())
#
#
# with conn:
#     curs = conn.cursor()
#     curs.execute('''select * from users where email like "%yandex.com" ''')
#     print(curs.fetchall())
#
# with conn:
#     curs = conn.cursor()
#     curs.execute('''delete from users where email like "%yandex.com" ''')
#     print(curs.fetchall())
#
# with conn:
#     curs = conn.cursor()
#     curs.execute('''select * from users limit 2''')
#     print(curs.fetchall())

# with conn:
#     curs = conn.cursor()
#     curs.execute('select id from USERS where id = {user_id}')
#     print(curs.fetchall())

with conn:
    conn.execute('''create table Posts (id integer unique primary key, 
    posts varchar(500))''')
