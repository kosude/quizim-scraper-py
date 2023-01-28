#
#   Copyright (c) 2023 Jack Bennett
#   All rights reserved.
#
#   Please see the LICENCE file for more information.
#

import os

def static_dir() -> str:
    return __path__[0]

def image_dir() -> str:
    return os.path.join(__path__[0], "img")
