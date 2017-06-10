#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


# Take the URL from Netlify's environment variable. If it's not set, default to no URL, which isn't
# great but at least won't break the site.
SITEURL = os.getenv('URL', '')
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
