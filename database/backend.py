from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/topics")
def topics():
    return render_template("topics.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
#Topics

if __name__ == "__main__":
    clear = lambda:os.system('cls')
    clear()
    app.run(debug=False)