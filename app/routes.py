#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import flask
from app import quizimapp, dirs
from app.session import *
from lib import *

# favicon route for compatibility
@quizimapp.route("/favicon.ico")
def favicon() -> flask.Response:
    return flask.send_from_directory(dirs.image(), "favicon.png")

# index: redirect to the homepage, assume javascript enabled
@quizimapp.route("/")
def index() -> flask.Response:
    return flask.render_template("index.html")

# home page
@quizimapp.route("/home")
def home() -> flask.Response:
    return flask.render_template("home.html")

# flashcards learning page
@quizimapp.route("/flashcards", methods=["GET", "POST"])
def flashcards() -> flask.Response:
    if flask.request.method == "POST":
        # clear to avoid exceeding maximum session cookie size
        flask.session.clear()

        id = flask.request.form["setid"]
        set_session_setid(id)

        url = get_set_url_from_id(id)
        set_session_cardset(scrape_quizlet_set(url))

        return flask.redirect(flask.url_for("flashcards"))

    return flask.render_template("flashcards.html", cardset=get_session_cardset(), setid=get_session_setid())
