#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Placeholder Author Who Does not Matter'
SITENAME = 'Institute of Medieval Music'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

THEME = 'theme'


# Change the URLs
# ===============
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = 'authors/index.html'
AUTHORS_URL = 'authors'
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
PAGE_URL = '{category}/{slug}'
PAGE_SAVE_AS = '{category}/{slug}/index.html'


# Theme (Pelican Settings)
# ========================
THEME_STATIC_DIR = 'static'
TYPOGRIFY = True
TEMPLATE_PAGES = {
    'series.html': 'series/index.html',
    'volumes.html': 'volumes/index.html',
}


# Theme (Custom Settings)
# =======================
