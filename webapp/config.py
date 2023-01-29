#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import os
from webapp import app, dirs

# secret key for csrf protection
CSRF_SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = CSRF_SECRET_KEY

# override static route
app.static_folder = dirs.static()

# HTML/jinja templates folder
app.template_folder = dirs.templates()

# session cookie config
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE="Lax"
)
