
# import os from the standard python library. We will use it to get our
# environment details

import os

# import json libary when using json data
import json

# small 'f' for first flask, capital 'F' for 2nd Flask - the capital indicates a
# class. 
# Import render_template function for rendering pages in html
# Import request function for handling things like what methods we used and it will also
# contain our form object when we've posted it.
# Import flash function to allow us to display non-permanent messages to the user.
# These are called flashed messages in Flask

from flask import Flask, render_template, request, flash

# Create an instance of this class, and store it in a variable called "app"
# Convention dictates that it be called "app"
# The first argument of the Flask class is the name of the applications module -
# our package. Since we're just using a single package we can just use __name__
# which is a built-in Python variable. Flask needs this so that it knows where
# to look for templates and static files

app = Flask(__name__)

# To use flashed messages we need to use a secret key, because Flask 
# cryptographically signs all of the messages for security. 
# Generally in production the secret key would be kept private.

app.secret_key ="some_secret"

# Use the route decorator to tell Flask what URL should trigger the function
# A decorator starts with the "@" sign, and is also called pie notation. A
# decorator is a way of wrapping functions (just as in JavaScript all functions
# are objects and can be passed around). So, when we try to browse to the root
# directory as indicated by the "/" then flask will trigger the index function
# underneath and return the "Hello World"

# This route decorator wraps around the "index" function. The "/" indicates the
# root directory. When we try to browse to it flask will trigger the "index"
# function, which will return "Hello World". The href for 'home' in index.html
# will be "/"

@app.route("/")
def index():
    return render_template("index.html")
    
# This route decorator wraps around the about(). The href for the about page 
# will be "/about"
# "page_title" (this could be any name) is a variable that will be passed to the
# page
# "list_of_numbers" = standard python list
    
@app.route("/about")
def about():
    
    # Initialise an empty array
    data = []
    
    # open the company.json file, read only
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    
    # return the company data to about.html
    return render_template("about.html", page_title="About", company=data)
    
# We want to open a member page, when the member name is clicked on
@app.route("/about/<member_name>")
def about_member(member_name):
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
                
# We want to open a member page, when the member name is clicked on
    return render_template("member.html", member=member)
    
# "page_title" (this could be any name) is a variable that will be passed to the
# page
# We need to tell the view what methods we can use, to allow us to send a message

@app.route("/contact", methods=["GET", "POST"])
def contact():

# The request function is imported above from flask
# It knows what methods we use and contains an object of the form we post

    if request.method == "POST":
        flash("Thanks {}. We have received your message".format(request.form["name"]))
    
    return render_template("contact.html", page_title="Contact")

# "page_title" (this could be any name) is a variable that will be passed to the
# page    
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

# If name = main we will run our app with the following arguments:
# "IP" is an internal variable set by Cloud9; os will get it for us. The same is
# true of "PORT", but it needs to be cast as an integer.
# Debug = True will help us debug our code

# NOTE!!!! Debug=True should be removed or be made "=False"??, before submitting
# Project for assessment, or releasing to production in a work environment.
# The variable __name__ will be = "__main__"

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port = int(os.environ.get("PORT")),
    debug=True)
    
    
    
