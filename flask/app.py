from flask import Flask, render_template
from flask import Flask, request,session

import random

#### The beginning of this one
  
app = Flask(__name__)
app.secret_key="something"

# Example of a route that passes
# data to a template
@app.route("/rand")
def randomnumber():
  i = random.randrange(100)
  return render_template("lucky.html",number = i )

# the "root" route
@app.route("/")
def index():
  return "<h1>Hello World from my computer! This is Mr. Wally. I will be graduating at the end of this semester. I am Practicing with Flask!</h1>"

# return a template 
@app.route("/about")
def about():
  return render_template("about.html")

# example of static content
# like an image or including css
@app.route("/image_css")
def image_css():
  return render_template("image_css.html")
  
  # this is where you define the form
  
@app.route("/form_demo",methods=['GET','POST'])
def form_demo():
  # GET is when we just load the page in our browser
  # POST is when we click the button 
  if request.method=="GET":
    return render_template("form_demo.html")
  else:
    # here we clicked the button
    # so we can check the form data
    name = request.form['username']
    pw = request.form['password']
    print(name,pw)
    if pw != "Teacher":
      # can change error message to: try again
      error = "BAD PASSWORD"
      name=""
    else: 
      error = ""
      
    return render_template("form_demo.html",error=error, name=name)

@app.route("/session_demo")
def session_demo():

  print(session)
  if 'count' not in session:
    session['count'] = 1
  else:
    session['count'] = session['count'] + 1

  return render_template('session_demo.html',count = session['count'])
 
  
app.run(host="0.0.0.0",port=5000,debug=True)