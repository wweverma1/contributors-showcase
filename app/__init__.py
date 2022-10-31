# Related third party imports
from flask import Flask

app = Flask(__name__)

from app.home.routes import home_api
from app.showcase.routes import showcase_api

app.register_blueprint(home_api)
app.register_blueprint(showcase_api)

from app.utils.app_functions import (
    before_request,
    after_request,
)