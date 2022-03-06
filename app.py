from flask import Flask


# The app factory function is the main entry point for the application.
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'


# __name__ serves for the purpose of running the application as a module or as a script.
if __name__ == '__main__':
    app.run(debug=True)
