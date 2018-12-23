#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
This plugin filters the "title" field so that it can be used to produce a sorted order that makes
sense to humans. The sortable title is added as the "title_sort" field.

This is what it does:
1.) converts to lowercase
2.) removes HTML tags
3.) trims leading/trailing whitespace
4.) removes leading articles (see list below)
5.) removes whitespace


**Copyright Notice**

This file contains code copied from the Pelican project ("generators.py") and modified for use by
the Institute of Mediaeval Music. The copyright of this file is therefore the same as the copied
source file, AGPLv3.
"""

from html.parser import HTMLParser
import re

from pelican import signals


# This list contains words that, if found at the start of the title, will be removed.
_DEFAULT_IGNOREABLE_INITIAL_WORDS = ('a', 'an', 'the')


class FilterTagsParser(HTMLParser):
    """
    Filters everything except HTML tag content.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = ''

    def handle_data(self, data):
        self.result += data


def add_title_sort(content):
    """
    Adds the "title_sort" field to every :class:`Content` page that has "title."
    """
    sort = ''

    if content.title:
        sort = content.title

        # pre: clean the ignoreable words too
        ignoreables = [
            word.lower().strip() for word in content.settings.get(
                'IGNOREABLE_INITIAL_WORDS',
                _DEFAULT_IGNOREABLE_INITIAL_WORDS
            )
        ]

        # 1.) converts to lowercase
        sort = sort.lower()

        # 2.) removes HTML tags
        parser = FilterTagsParser()
        parser.feed(sort)
        parser.close()
        sort = parser.result

        # 3.) trims leading/trailing whitespace
        sort = sort.strip()

        # 4.) removes leading articles(see list below)
        index_of_first_space = sort.find(' ')
        if index_of_first_space != -1 and sort[0:index_of_first_space] in ignoreables:
            sort = sort[index_of_first_space:]

        # 5.) removes whitespace
        sort = re.sub(r'\W', '', sort)

    content.title_sort = sort

    if len(content.title_sort) > 0:
        content.title_sort_initial = content.title_sort[0]
    else:
        content.title_sort_initial = ''


def register():
    """
    Connect the Pelican signals.
    """
    signals.content_object_init.connect(add_title_sort)
