#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import flask
from app import quizimapp, dirs

# accessing images (shorthand; essentially the same as /static/img/...)
# (images)
@quizimapp.route("/img/<path:filename>")
def image_serve(filename: str) -> flask.Response:
    return flask.send_from_directory(dirs.image(), filename)

# favicon route for compatibility
@quizimapp.route("/favicon.ico")
def favicon() -> flask.Response:
    return flask.send_from_directory(dirs.image(), "favicon.png")
