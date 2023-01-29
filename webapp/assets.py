#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

from flask_assets import Bundle
from webapp import quizimassets, dirs

quizimassets.url = "/static"
quizimassets.directory = dirs.static()

# Sass/SCSS asset compilation + bundling
scss = Bundle(
    "scss/main.scss",
    depends=("scss/**/*.scss"),
    filters="pyscss",
    output="out/style.css"
)
quizimassets.register("all_scss", scss)
