from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "will this work this time"

if __name__ == "__main__":
    app.run()
