from flask import Blueprint

from app.showcase.controller import (
    generate_contributors_showcase,
)

showcase_api = Blueprint('showcase', __name__)

showcase_api.add_url_rule(rule='/showcase', view_func=generate_contributors_showcase, methods=['GET', ])