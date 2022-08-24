from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "i have restarted"

@app.route("/about")
def about():
    return "<h1 style='color:red'> about</h1>"


@app.route("/date")
def date():
     return "mikes index:<strong>22JL30+461055</strong>"

if __name__ =="__main__":
    app.run()
