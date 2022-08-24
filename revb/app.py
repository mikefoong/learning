from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "initialise flask index"

@app.route("/about")
def about():
    return "<h1 style='color: red'> this is the about page</h1>"

@app.route("/mikeindex")
def mikesIndex():
    return "logIndex:<strong>2022JL31+460723</strong≈>>"

if __name__ == "__main__":
    app.run()
