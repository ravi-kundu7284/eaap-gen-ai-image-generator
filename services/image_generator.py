from flask import render_template
import os

openai_api_key = os.getenv("OPENAI_API_KEY")


# @app.route("/")
def home():
    return render_template("index.html")
