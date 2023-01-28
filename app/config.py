#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import os
from app import quizimapp
from views import templates_dir

# secret key for csrf protection
CSRF_SECRET_KEY = os.urandom(32)
quizimapp.config["SECRET_KEY"] = CSRF_SECRET_KEY

# override static route
quizimapp.static_folder = None

# HTML/jinja templates folder
quizimapp.template_folder = templates_dir()
