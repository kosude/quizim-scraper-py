#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

from flask import Flask
from flask_assets import Environment

app = Flask("quizimapp")
quizimassets = Environment(app)

import webapp.config
import webapp.assets
import webapp.routes
