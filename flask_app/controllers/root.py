from flask import render_template
from flask_app import app

@app.route("/", methods=["GET"])
def show_index():
  return render_template("index.html")

@app.route("/about", methods=["GET"])
def show_about():
  return render_template("about.html")
