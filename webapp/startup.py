#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import os
import flask
from flask_assets import Environment, Bundle
from .utils import *
from lib import *


#
## configure application

app = flask.Flask("quizimapp")

app.template_folder = dirs.templates(app.root_path)
app.static_folder = dirs.static(app.root_path)

# secret key for csrf protection
CSRF_SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = CSRF_SECRET_KEY

# session cookie config
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE="Lax"
)


#
## register assets to be compiled and/or bundled

quizimassets = Environment(app)
quizimassets.cache = False
quizimassets.manifest = False

quizimassets.url = "/static"
quizimassets.directory = dirs.static(app.root_path)

# Sass/SCSS asset compilation + bundling
scss = Bundle(
    "scss/main.scss",
    depends=("scss/**/*.scss"),
    filters="pyscss",
    output="out/style.css"
)
quizimassets.register("all_scss", scss)


#
## configure HTTP routes

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
