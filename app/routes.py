#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import flask
from app import quizimapp

# index/root page
@quizimapp.route("/")
def index() -> flask.Response:
    return flask.render_template("index.html")
