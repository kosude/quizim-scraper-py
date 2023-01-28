#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import flask
from app import quizimapp
import static

# accessing images
# (images)
@quizimapp.route("/img/<path:filename>")
def image_serve(filename: str) -> flask.Response:
    return flask.send_from_directory(static.image_dir(), filename)

# accessing other static stuff
# (css, js, etc...)
@quizimapp.route("/static/<path:filename>")
def static_serve(filename: str) -> flask.Response:
    return flask.send_from_directory(static.static_dir(), filename)

# favicon route for compatibility
@quizimapp.route("/favicon.ico")
def favicon() -> flask.Response:
    return flask.send_from_directory(static.image_dir(), "favicon.png")
