from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import models


# The app factory function is the main entry point for the application.
app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        db_password = models.check_password(username)
        if password == db_password:
            message = models.show_name(username)
            return render_template('about.html', message=message)
        else:
            return render_template('index.html', message='Invalid credentials!')


@ app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


# __name__ serves for the purpose of running the application as a module or as a script.
if __name__ == '__main__':
    app.run(debug=True, port=7000)
