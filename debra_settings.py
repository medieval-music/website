#!/usr/bin/env python
# -*- coding: utf-8 -*- #

"""
This files holds settings that Debra can change without much fear.

A little bit of fear is okay though: this is a Python file, and we're just going to use it to
store some settings, but you could mess things up if you're not careful!


How to Use this File
--------------------

Here's an example of how the settings work. So far, we're always mapping one version of something
to another version of that thing. The generic way it works is like this:

TYPE_OF_THING_BEING_MAPPED = {
    'this thing': 'becomes this thing',
    'that thing': 'becomes this thing',
}

In this case, whenever we find a "this thing" OR a "that thing," because of this configuration,
it will always be mapped to "becomes this thing." A more concrete example:

AUTHOR_TO_CANONICAL = {
    'Sally B. Johnson': 'Sally Johnson',
    'Sally B. F. Johnson': 'Sally Johnson',
}

In this case, we're mapping "Sally B. Johnson" and "Sally B. F. Johnson" to the canonical name
"Sally Johnson." Because "Sally Johnson" isn't in that settings object, we'll assume it's already
in the canonical form.

There are a few simple rules:

- Each setting line starts with four spaces.
- The "from" value (input) and "to" value (output) are both surrounded by single-quote marks.
- The "from" and "to" values are separated with a colon.
- Each setting line ends with a comma.


Description of Settings
-----------------------
- SERIES_NAMES maps a directory name in "content/pages" to the full name of that series.
- AUTHOR_TO_CANONICAL maps various spellings (forms, versions) of an author's name to a canonical
  version. The canonical version is used in the "Authors" list, though each book page uses the
  spelling in its own file.
- HOMEPAGE_IMAGE_CREDIT is the text shown below the manuscript image on the homepage. Make sure
  this text begins and ends with a triple-double-quote like on the next line:
"""

SERIES_NAMES = {
    'collected_works': 'Collected Works',
    'de_medicinae_rebus': 'De Medicinæ Rebus',
    'in_translation': 'Musical Theorists in Translation',
    'manuscripts': 'Publications of Mediæval Musical Manuscripts',
    'studies': 'Musicological Studies',
}

AUTHOR_TO_CANONICAL = {
    'Gillingham, B.': 'Gillingham, Bryan',
    'Santosuosso, Alma': 'Santosuosso, Alma Colk',
    'Boyce, James': 'Boyce, James (O. Carm.)',
    'Haggh, Barbara': 'Haggh-Huglo, Barbara',
    'Lacoste, Debra': 'Lacoste, Debra S.',
}

HOMEPAGE_IMAGE_CREDIT = """Photograph courtesy of Wilfrid Laurier University Archives."""
