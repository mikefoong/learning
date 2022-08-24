from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "finally getting it right?"

@app.route('/about')
def about():
    return "<h1 style='color: red'> about </h1> <br><p>this is revision E. took me more than 5 times to get it right"

@app.route('/mikesindex')
def mikesindex():
    return "22Au090+46723"

if __name__ == "__main__":
    app.run()