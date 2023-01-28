#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

from flask import Flask
from flask_assets import Environment

quizimapp = Flask("quizimapp")
quizimassets = Environment(quizimapp)

import app.config
import app.assets
import app.routes
