import logging
from flask import Flask
from loader.loader import post_blueprint
from main.main import main_blueprint

logging.basicConfig(format='%(levelname)s:%(asctime)s:%(message)s', filename="logs/main.log", level=logging.DEBUG)

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)

app.run()
