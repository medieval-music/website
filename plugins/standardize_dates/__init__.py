#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
TODO: write this plugin


**Copyright Notice**

This file contains code copied from the Pelican project ("generators.py") and modified for use by
the Institute of Mediaeval Music. The copyright of this file is therefore the same as the copied
source file, AGPLv3.
"""

import datetime

from pelican import signals


def add_title_sort(content):
    """
    Add the "imm_year" and "imm_date" fields to every :class:`Content` page.
    """

    has_date = hasattr(content, 'date')
    has_year = hasattr(content, 'year')

    # Default in case there's simply no date. Mark it all as None.
    content.imm_date = None
    content.imm_year = None

    if has_date and has_year:
        # Largely theoretical concern that a volume may have both "date" and "year"
        # specified. As of Februry 2020, this isn't true for any of the volumes.
        content.imm_date = content.year
        content.imm_year = content.date.year

    elif has_date:
        # If there's a date but no year, we can easily get the year.
        content.imm_date = content.date
        content.imm_year = str(content.date.year)

    elif has_year:
        # If there's a year but no date, we can assume a date.
        content.imm_date = datetime.date(int(content.year), 1, 1)
        content.imm_year = content.year


def register():
    """
    Connect the Pelican signals.
    """
    signals.content_object_init.connect(add_title_sort)
