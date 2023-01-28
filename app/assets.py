#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import flask
from flask_assets import Bundle
from app import quizimassets
import static

quizimassets.url = "/static"
quizimassets.directory = static.static_dir()

# Sass/SCSS asset compilation + bundling
scss = Bundle(
    "scss/main.scss",
    depends=("scss/**/*.scss"),
    filters="pyscss",
    output="out/style.css"
)
quizimassets.register("all_scss", scss)
