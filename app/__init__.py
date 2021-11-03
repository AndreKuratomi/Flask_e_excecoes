import json
from flask import Flask, request
from dotenv import load_dotenv
from user_register_modes.register_modes import read_register, register_user

app = Flask(__name__)

load_dotenv()



@app.get("/user")
def decorated_read_registers():
    return read_register()


@app.post("/user")
def decorated_register_user():
    name = request.data["name"]
    email = request.form["email"]
    return register_user(name, email)
