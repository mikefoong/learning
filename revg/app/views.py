from app import app

from flask import render_template

@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/about')
def about():
    return "<h1 style='color:red'>About</h1>"

@app.route('/mikesindex')
def mikesindex():
    return "2022Au09+461809:static files"

@app.route('/dashboard')
def dashboard():
    return render_template("admin/dashboard.html")