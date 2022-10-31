# Related third party imports
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

from app.home.routes import home_api
from app.showcase.routes import showcase_api

app.register_blueprint(home_api)
app.register_blueprint(showcase_api)

from app.utils.app_functions import (
    before_request,
    after_request,
)