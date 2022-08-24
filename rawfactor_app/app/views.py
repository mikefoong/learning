from app import app

@app.route("/")
def update():
    return "i am on my own "