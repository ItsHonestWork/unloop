# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://itshonestwork.github.io/unloop/"
RELATIVE_URLS = False

FEED_ALL_ATOM = ""
CATEGORY_FEED_ATOM = ""

DELETE_OUTPUT_DIRECTORY = True