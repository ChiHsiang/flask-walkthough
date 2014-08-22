from flask import render_template, request, redirect, session, flash
from flask_app import app

@app.route("/sign-in", methods=["GET"])
def show_sign_in():
  return render_template("sign-in.html")

@app.route("/sign-in", methods=["POST"])
def sign_in():
  session["email-address"] = request.form["email-address"]
  flash("You've successfully signed in")
  return redirect("/")

@app.route("/sign-out", methods=["GET"])
def sign_out():
  del session["email-address"]
  flash("You've signed out")
  return redirect("/")
