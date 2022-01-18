from django.shortcuts import render
from flask import Flask, render_template
from flask_session import Session
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")
