import os
import json
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["GET"])
def show_index():
  return render_template("index.html")

@app.route("/about", methods=["GET"])
def show_about():
  return render_template("about.html")

@app.route("/sign-in", methods=["GET"])
def show_sign_in():
  return render_template("sign-in.html")

@app.route("/sign-in", methods=["POST"])
def sign_in():
  raise NotImplementedError()

@app.route("/sign-out", methods=["GET"])
def sign_out():
  raise NotImplementedError()

def load_config(app, relative_path, environment):
  config = None
  with open(os.path.join(app.root_path, relative_path), "r") as rf:
    config = json.load(rf)
  app.config.update(config[environment])
