from flask import Flask
app = Flask(_name_)
@app.route('/')
def welcome():
    return "this is my first Flask app! Yay"
print(app.run_