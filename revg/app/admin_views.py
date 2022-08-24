from app import app
from flask import render_template

@app.route('/dashboard')
def admmin_dashboard():
    return render_template("admin/dashboard.html")

@app.route('/profile')
def profile():
    return "<h1 style='color:red'>Profile</h1>"

@app.route('/plain')
def plain():
    return "2022Au09+461741: serving html" 