#!/usr/bin/python3
"""
This module is about the blueprint of the API
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__)
from api.v1.views.index import *  # noqa: E402
from api.v1.views.states import *  # noqa: E402
from api.v1.views.cities import *  # noqa: E402
