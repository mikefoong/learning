from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return" this is revision C"

@app.route("/about")
def about():
    return "<h1 style='color: red'>about</h1>"

@app.route("/mikesindex")
def mikesindex():
    return "2022Au09+460030"

if __name__ =="__main__":
    app.run()

