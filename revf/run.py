from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "Revision F. got the proper sequence now!"

@app.route('/about')
def about():
    return "<h1 style='color: red'> about</h1>"

@app.route('/mikesindex')
def mikesindex():
    return "2022Au09+462228"
    
if __name__ == '__main__':
    app.run()