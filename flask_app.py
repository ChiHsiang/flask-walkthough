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

if __name__ == "__main__":
    app.debug = True
    app.run()
