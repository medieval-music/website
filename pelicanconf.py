#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys

try:
    sys.path.append(os.curdir)
    from debra_settings import *
except SyntaxError:
    print('\n\nPROBLEM: There is a syntax mistake in "debra_settings.py"\n\n')
    raise


AUTHOR = 'Placeholder Author Who Does not Matter'
SITENAME = 'Institute of Mediaeval Music'
RELATIVE_URLS = False
# used when no author or editor is in the record
INSTITUTION_AUTHOR = SITENAME

# If this is a branch deploy (i.e., not the "main" branch) then we want to use
# Netlify's "prime URL." If it's the "main" branch then we want to use the
# proper URL. This also works if we're building locally because "prime_url"
# defaults to an empty string.
prime_url = os.getenv('DEPLOY_PRIME_URL', '')
if prime_url.startswith('https://main--'):
    SITEURL = os.getenv('URL', '')
else:
    SITEURL = prime_url

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

SLUGIFY_SOURCE = 'basename'
DEFAULT_METADATA = {
    'isbn13': 'DEFAULT ISBN-13 PLACEHOLDER',
    'series': 'DEFAULT SERIES THAT WE SHOULD NOT SHOW',
    'volume': 'DEFAULT VOLUME THAT WE SHOULD NOT SHOW',
    'volume_part': 'DEFAULT VOLUME PART THAT WE SHOULD NOT SHOW',
}
PATH_METADATA = r'pages/(?P<series>.*)/(?P<isbn13>\d{3}-\d-\d{6}-\d{2}-\d)\.rst'

PLUGINS = [
    'plugins.combine_authors',
    'plugins.standardize_dates',
    'plugins.title_sort',
    'plugins.volume_sort',
]

ARTICLE_PATHS = ['news']


# Change the URLs
# ===============
ARCHIVES_SAVE_AS = ''
ARTICLE_SAVE_AS = ''
AUTHORS_SAVE_AS = 'authors/index.html'
AUTHORS_URL = 'authors'
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''
PAGE_URL = 'books/{slug}'
PAGE_SAVE_AS = 'books/{slug}/index.html'


# Theme (Pelican Settings)
# ========================
DIRECT_TEMPLATES = ['authors']
THEME_STATIC_DIR = 'static'
TYPOGRIFY = True
TEMPLATE_PAGES = {
    'news.html': 'news/index.html',
    'series.html': 'series/index.html',
    'titles.html': 'titles/index.html',
}


# Theme (Custom Settings)
# =======================

# desired width, in pixels, for the homepage image to be outputted in
HOMEPAGE_IMAGE_SIZES = os.getenv('HOMEPAGE_IMAGE_SIZES', '300 400 500 600 700').split(' ')
