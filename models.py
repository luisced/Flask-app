import sqlite3


def show_name(username):
    connection = sqlite3.connect('first_database.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT lastname FROM users WHERE username = '{username}' ORDER BY id DESC;""".format(username=username))
    last_name = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    message = 'Welcome {username} {last_name}'.format(
        username=username, last_name=last_name)
    return message


def check_password(username):
    connection = sqlite3.connect('first_database.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """SELECT password FROM users WHERE username = '{username}' ORDER BY id DESC;""".format(username=username))
    password = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()
    return password
