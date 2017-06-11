#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
This plugin converts the "volume" and "volume_part" fields into an integer that can be used to sort
all the volumes in a series. This integer is added to the "volume_sort" field.


**Copyright Notice**

This file contains code copied from the Pelican project ("generators.py") and modified for use by
the Institute of Mediaeval Music. The copyright of this file is therefore the same as the copied
source file, AGPLv3.
"""

import itertools
import logging

from pelican import contents, generators, signals, urlwrappers
import roman

# We multiply the different parts of the volume number by a different factor in order to consider
# the different priority of the different parts. That is: the volume number is large enough that
# the volume part won't interfere (unless there is a volume with more than 1000 parts) and the
# volume part number is large enough that the volume part letter won't interfere.
#
# Description of the parts of the volume number:
#     Volume 42/6b
#     - 42 is the "volume number"
#     - 6 is the "volume part number"
#     - b is the "volume part letter"
#

_VOLUME_FACTOR = 100000
_VOLUME_PART_FACTOR = 1000
_VOLUME_PART_LETTER_FACTOR = 1
_ORD_OFFSET = ord('A')  # helps ensure any single letter will add less than 100


def add_volume_sort(content):
    """
    Adds the "volume_sort" field to every :class:`Content` page that has "volume."
    """
    sort = 0

    if content.volume != 'DEFAULT VOLUME THAT WE SHOULD NOT SHOW':
        sort += roman.fromRoman(content.volume) * _VOLUME_FACTOR

    if content.volume_part != 'DEFAULT VOLUME PART THAT WE SHOULD NOT SHOW':
        try:
            sort += int(content.volume_part) * _VOLUME_PART_FACTOR
        except ValueError:
            sort += int(content.volume_part[:-1]) * _VOLUME_PART_FACTOR
            sort += (ord(content.volume_part[-1]) - _ORD_OFFSET) * _VOLUME_PART_LETTER_FACTOR

    content.volume_sort = sort


def add_multipart_volumes(page_generator):
    """
    **Output Format**

    An object with the following shape is attached to the global "context" as "multipart_volumes".

    [
        {
            'series': 'manuscripts',
            'series_name': 'Publications of Mediæval Musical Manuscripts',
            'volumes': [
                {
                    'volume': 'VIII',
                    'books': [
                        <pelican.contents.Page object at ...>,
                        <pelican.contents.Page object at ...>,
                        <pelican.contents.Page object at ...>,
                    ],
                },
            ],
        },
    ]

    Notes:

    - The outermost "series" list is sorted by "series_name."
    - If "series_name" is not set, "series" is used.
    - The "volumes" list is sorted by volume number.
    - The "books" list is sorted by volume number (that is: by volume part).
    - Series with no multi-part volumes are omitted.
    - Books assigned to the default series are omitted.
    """
    multipart_volumes = []

    # groupby() requires sorting first
    sorted_pages = sorted(page_generator.pages, key=lambda x: x.series)
    grouped_pages = itertools.groupby(sorted_pages, lambda x: x.series)

    for series, group in grouped_pages:
        if series == page_generator.settings['DEFAULT_METADATA']['series']:
            continue

        this_series = {
            'series': series,
            'series_name': page_generator.settings['SERIES_NAMES'].get(series, series),
            'volumes': [],
        }

        # groupby() requires sorting first... and we're being sneaky by sorting with a *different*
        # key than we use for grouping. This allows us to get the proper Roman numeral order when
        # sorting, but to still do the grouping by volume without considering volume_part.
        sorted_by_volume = sorted(group, key=lambda x: x.volume_sort)
        grouped_by_volume = itertools.groupby(sorted_by_volume, lambda x: x.volume)

        for volume, pages in grouped_by_volume:
            list_of_pages = list(pages)
            if len(list_of_pages) > 1:
                this_series['volumes'].append({
                    'volume': volume,
                    'books': sorted(list_of_pages, key=lambda x: x.volume_sort),
                })

        if len(this_series['volumes']) > 1:
            multipart_volumes.append(this_series)

    # The "series" and "series_name" probably have different sort orders, so we must do this again.
    multipart_volumes = sorted(multipart_volumes, key=lambda x: x['series_name'])
    page_generator.context['multipart_volumes'] = multipart_volumes


def register():
    """
    Connect the Pelican signals.
    """
    signals.content_object_init.connect(add_volume_sort)
    signals.page_generator_finalized.connect(add_multipart_volumes)
