import os
from flask import Blueprint, Flask, abort, session, request, redirect
from flask_wtf.csrf import CSRFProtect
from flask_restx import Resource, Api, fields
from flask.json import jsonify

app = Flask(__name__, template_folder="../public",
            static_folder="../public", static_url_path='')

app.config['ERROR_404_HELP'] = False
# csrf = CSRFProtect(app)

blueprint = Blueprint('api', __name__, url_prefix='/v1')
api = Api(blueprint,
          title="My API",
          version='v0.1',
          description='Description'
          )
app.register_blueprint(blueprint)

from server.routes import *  # noqa


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
