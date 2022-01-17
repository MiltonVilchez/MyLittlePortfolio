from flask import Flask
from flask_session import Session
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def hello():
    return "Hello, World!"
