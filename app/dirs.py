#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import os
from app import quizimapp

# static/ folder path.
# Includes SCSS, JS, etc...
def static() -> str:
    return os.path.join(quizimapp.root_path, "static")

# static/img/ folder path.
# includes image resources
def image() -> str:
    return os.path.join(quizimapp.root_path, "static", "img")

# views/ folder path.
# includes HTML/jinja2 components and templates.
def templates() -> str:
    return os.path.join(quizimapp.root_path, "views")
