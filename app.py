from flask import Flask
app = Flask(__name__)
@app.route('/')
def welcome():
    return "this is my first Flask app! Yay"
if __name__ == '__main__':
 app.run()
