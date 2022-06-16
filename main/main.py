import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request, abort
from jinja2 import TemplateNotFound

from functions import JsonLoader

# Log configuration settings
FORMAT = '%(asctime)s %(clientip)-15s %(message)s'
logging.basicConfig(format=FORMAT, filename="logs/main.log", level=logging.DEBUG)

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")
POSTS = JsonLoader('posts.json')


@main_blueprint.route('/')
def main():
    """Returns main page"""
    return render_template('index.html')


@main_blueprint.route('/search')
def search():
    """Returns search page, lookup is a keyword for search request"""
    try:
        # getting a keyword
        lookup = request.args.get('s')
        # creating a list of objects based on a keyword
        result_of_search = POSTS.load_from_json_by_value(value=lookup)
        logging.info(f"Searched for {lookup}")
        return render_template('post_list.html', lookup=lookup, result=result_of_search)
    except TemplateNotFound:
        logging.info("Template was not found")
        abort(404)
    except JSONDecodeError:
        logging.error(f"Couldn't refactor JSON file")
        return f"Couldn't refactor JSON file"
