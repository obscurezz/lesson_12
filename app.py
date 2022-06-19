import logging
from os import path, mkdir

from flask import Flask, send_from_directory

from loader.loader import post_blueprint
from main.main import main_blueprint
from settings import LOGS_FOLDER

if not path.exists(LOGS_FOLDER):
    mkdir(LOGS_FOLDER)

FORMAT = '%(levelname)s:%(asctime)s - - %(message)s'
logging.basicConfig(format=FORMAT, encoding='utf-8', filename="logs/main.log", level=logging.DEBUG)

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)


@app.route("/uploads/images/<path:path>")
def static_dir(path):
    return send_from_directory("uploads/images", path)


app.run()
