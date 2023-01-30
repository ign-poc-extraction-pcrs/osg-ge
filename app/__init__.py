from flask import Flask
from app.controllers import route


app = Flask(__name__)

app.register_blueprint(route.route)
