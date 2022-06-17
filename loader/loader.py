import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort
from jinja2 import TemplateNotFound

from functions import JsonLoader, create_content_dict, is_filename_allowed


post_blueprint = Blueprint('post_blueprint', __name__, template_folder="templates")
POSTS = JsonLoader('posts.json')
UPLOAD_FOLDER = "./uploads/images"


@post_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html')


@post_blueprint.route('/post', methods=["GET", "POST"])
def page_post_upload():
    try:
        # Text data from html form to json
        content = request.form.get('content')

        # Image data from html to json
        picture = request.files.get('picture')
        picture_filename = picture.filename

        # Check if uploaded file is not an image
        if is_filename_allowed(picture_filename):
            picture.save(f"{UPLOAD_FOLDER}/{picture_filename}")
        else:
            logging.info(f'Extension {picture_filename.split(".")[-1]} is not allowed')
            return f'Extension {picture_filename.split(".")[-1]} is not allowed'

        # Creating a dict and uploading it to json
        post: dict = create_content_dict(f"{UPLOAD_FOLDER}/{picture_filename}", content)
        POSTS.upload_data_to_json(post)

        return render_template('post_uploaded.html', post=post)
    except TemplateNotFound:
        logging.info("Template was not found")
        abort(404)
    except JSONDecodeError:
        logging.error("Couldn't refactor JSON file")
        return f"Couldn't refactor JSON file"
    except (FileExistsError, FileNotFoundError):
        logging.error("Something is wrong with the file")
        return f"Something is wrong with the file"
