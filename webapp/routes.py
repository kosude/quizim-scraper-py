#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import flask
from webapp import app, dirs
from webapp.session import *
from lib import *

# favicon route for compatibility
@app.route("/favicon.ico")
def favicon() -> flask.Response:
    return flask.send_from_directory(dirs.image(), "favicon.png")

# index: redirect to the homepage, assume javascript enabled
@app.route("/")
def index() -> flask.Response:
    return flask.render_template("index.html")

# home page
@app.route("/home")
def home() -> flask.Response:
    return flask.render_template("home.html")

# flashcards learning page
@app.route("/flashcards", methods=["GET", "POST"])
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
