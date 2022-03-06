import sqlite3 as sql
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# check_same_thread=False allows to run the app in multiple threads
connection = sql.connect('first_database.db', check_same_thread=False)
cursor = connection.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT(50) NOT NULL,
    name TEXT(100) NOT NULL,
    lastname TEXT(100) NOT NULL,
    email TEXT(100) NOT NULL,
    password TEXT(32) NOT NULL
);""")

connection.commit()
cursor.close()
connection.close()
