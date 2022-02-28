from flask import Flask, render_template

import random

app = Flask(__name__)

@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  return render_template("lucky.html",number = i)

@app.route("/")
def index():
  return "<h1>Hello World from my computer! This is Mr. Wally. I will be graduating at the end of this semester.</h1>"


app.run(host="0.0.0.0",port=5000,debug=True)