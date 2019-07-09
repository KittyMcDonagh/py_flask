
# import os from the standard python library. We will use it to get our
# environment details

import os

# small 'f' for first flask, capita'F' for 2nd Flask - the capital indicates a
# class

from flask import Flask

# Create an instance of this class, and store it in a variable called "app"
# Convention dictates that it be called "app"
# The first argument of the Flask class is the name of the applications module -
# our package. Since we're just using a single package we can just use __name__
# which is a built-in Python variable. Flask needs this so that it knows where
# to look for templates and static files

app = Flask(__name__)

# Use the route decorator to tell Flask what URL should trigger the function
# A decorator starts with the "@" sign, and is also called pie notation. A
# decorator is a way of wrapping functions (just as in JavaScript all functions
# are objects and can be passed around). So, when we try to browse to the root
# directory as indicated by the "/" then flask will trigger the index function
# underneath and return the "Hello World"

# This route decorator wraps around the "index" function. The "/" indicates the
# root directory. When we try to browse to it flask will trigger the "index"
# function, which will return "Hello World"

@app.route("/")
def index():
    return "Hello World"

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
    
    
    
