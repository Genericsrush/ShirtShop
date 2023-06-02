from flask import Flask, render_template

# This code defines the application instance for the flask framework.
app = Flask(__name__)


# These are the routes for the flask application.

# This is the index route.
@app.route("/")
def index():
    name = "Macray"
    return render_template('index.html', title="Hello", username=name)