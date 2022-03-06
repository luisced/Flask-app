from multiprocessing import connection
import sqlite3 as sql

connection = sql.connect('first_database.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(
    """ INSERT INTO users(
        username, name, lastname, email, password
        )
        VALUES(
            'Luisced02031', 'Luis', 'Cedillo', 'luisced02031@gmail.com', '12345678'
    );"""

)

cursor.execute(
    """ INSERT INTO users(
        username, name, lastname, email, password
        )
        VALUES(
            'user02021', 'user', 'userlastname', 'user@gmail.com', '12345678'
    );"""

)

connection.commit()
cursor.close()
connection.close()
