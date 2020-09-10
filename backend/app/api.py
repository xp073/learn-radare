from flask import Blueprint
def create_api():
    api = Blueprint(name=api, url_prefix="api")

    return api
