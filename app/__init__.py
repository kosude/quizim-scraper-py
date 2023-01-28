#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

from flask import Flask

quizimapp = Flask("quizimapp")

import app.config
import app.routes
import app.static_serve
