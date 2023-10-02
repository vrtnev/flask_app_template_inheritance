from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def name(name):
    return render_template("index.html", content=name, id=16)

if __name__ == "__main__":
    app.run(debug=True)