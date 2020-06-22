#!/usr/bin/env python
# -*- coding: utf-8 -*- #

'''
This files holds settings that Debra can change without much fear.

A little bit of fear is okay though: this is a Python file, and we could potentially do anything to
the website. So be wary of letting your neighbours edit this file! :)


How to Use this File
--------------------

So far we're using three data types for settings: mapping, sequence, and string. (And these are the
real words software developers use for Python!)

If you change a setting in this file and then regenerate the website, the new setting will be used.
You can add new settings to this file, but the result may not be easy to predict.


"Mapping" Settings
------------------

We use a "dictionary" as a "mapping" from one value to another. For example:

TYPE_OF_THING_BEING_MAPPED = {
    'this thing': 'item 1',
    'that thing': 'item 1',
    'other thing': 'item 2',
}

In this case, both "this thing" and "that thing" are mapped to "item 1". But "other thing" is
mapped to "item 2". There are a few rules:

- Each mapping line starts with four spaces.
- The "from" value (input) and "to" value (output) are both surrounded by single-quote marks.
- The "from" and "to" values are separated with a colon.
- Each setting line ends with a comma.


"Sequence" Settings
-------------------

We use a "list" as a "sequence" of items of the same type. For example:

TYPE_OF_THING_BEING_LISTED = [
    'first thing',
    'second thing',
    'third thing',
]

It's just a list of some items. There are a few rules:

- Each item line starts with four spaces.
- Each item is surrounded by single-quote marks.
- Each item line ends with a comma.

You can also make an empty list by removing all the items, like this:

TYPE_OF_THING_BEING_LISTED = [
]

This is like "turning off" the feature that uses that setting.


"String" Settings
-----------------

For our purposes, a "string" is a word, sentence, paragraph, or similar. For a string setting,
these start and end with three double-quote marks in a row, like this:

SOME_SENTENCE = """A"""

And then whatever you write between the sets of quote marks is what we use for the setting!


Description of Settings
-----------------------
- SERIES_NAMES maps a directory name in "content/pages" to the full name of that series.
- SERIES_ALT_NAMES maps a directory name in "content/pages" to a list of alternative
  names for that series (i.e., translations). This is optional, meaning you don't have
  to provide ALT_NAMES for every series.
- AUTHOR_TO_CANONICAL maps various spellings (forms, versions) of an author's name to a canonical
  version. The canonical version is used in the "Authors" list, though each book page uses the
  spelling in its own file.
- IGNOREABLE_INITIAL_WORDS is a list of words that, when they appear as the first word in a book
  title, will not be used when assigning alphabetical order for the title. For example, if "la" is
  in this list and we have a book called "La piscine des oiseaux," the book will be sorted among the
  other books whose titles start with the letter "p." The words here are case insensitive.
- HOMEPAGE_IMAGE_CREDIT is the text shown below the manuscript image on the homepage.
'''

SERIES_NAMES = {
    'collected_works': 'Collected Works',
    'de_medicinae_rebus': 'De Medicinæ Rebus',
    'in_translation': 'Musical Theorists in Translation',
    'manuscripts': 'Publications of Mediæval Musical Manuscripts',
    'studies': 'Musicological Studies',
}

SERIES_ALT_NAMES ={
    'collected_works': ['Gesamtausgaben'],
    'manuscripts': [
        'Veröffentlichungen mittelalterlicher Musikhandschriften',
        'Publications des manuscrits musicaux du moyen age'
    ],
    'studies': ['Wissenschaftliche Abhandlungen'],
}

AUTHOR_TO_CANONICAL = {
    'Boyce, James': 'Boyce, James (O. Carm.)',
    'van Deusen, Nancy': 'Deusen, Nancy van',
    'de Peñalosa, Francisco': 'Peñalosa, Francisco de',
    'Antoine de Févin': 'Févin, Antoine de',
    'de Févin, Antoine': 'Févin, Antoine de',
    'Robert de Févin': 'Févin, Robert de',
    'de Févin, Robert': 'Févin, Robert de',
    'Galliculus (Hähnel), Johannes': 'Galliculus (Alectorius, Hähnel, Hennel), Johannes',
    'Gillingham, B.': 'Gillingham, Bryan',
    'Del Giudice, Luisa': 'Giudice, Luisa del',
    'Haggh, Barbara': 'Haggh-Huglo, Barbara',
    'Hardie, Jane': 'Hardie, Jane Morlet',
    'Lacoste, Debra': 'Lacoste, Debra S.',
    'de Loos, Ike': 'Loos, Ike de',
    'Nelson, Kathleen': 'Nelson, Kathleen E.',
    'Santosuosso, Alma': 'Santosuosso, Alma Colk',
}

HOMEPAGE_IMAGE_CREDIT = """Photograph courtesy of Wilfrid Laurier University Archives."""

IGNOREABLE_INITIAL_WORDS = [
    'a',
    'an',
    'la',
    'le',
    'les',
    'of',
    'on',
    'the',
]
