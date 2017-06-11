#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
This plugin manipulates author- and editor-related metadata in several ways:

- First, the fields named "author," "author2," through "author9" are copied into the
  :attr:`imm_authors` attribute on a :class:`Content`.
- Also a similar thing for editors: "editor" through "editor9" are collected into the
  :attr:`imm_editors` attribute.
- If an author is the same as the default :const:`AUTHOR` setting, it is omitted. This may lead to
  :class:`Content` instances where :attr:`imm_authors` is empty.
- Finally, add an "imm_authors_list" list to the templating context (that is: as a variable
  accessible in the Jinja2 templates). Data format described below.


**Data Format for the Context Object**

The "imm_authors_list" context object looks like this:

    [
        {
            'author name': 'Lacoste, Debra',
            'author slug': 'lacoste-debra',
            'books': [
                {
                    'title': 'Doing Great Stuff',
                    'isbn13': '978-0-931902-92-5',
                    'is author': True,
                    'is editor': False,
                },
            ],
        },
    ]

And so on. Only one of "is author" or "is editor" will be True for each book, and the other will
be False. Note that the lists are sorted alphabetically: the author list by "author name" and each
book list by "title."


**Copyright Notice**

This file contains code copied from the Pelican project ("generators.py") and modified for use by
the Institute of Mediaeval Music. The copyright of this file is therefore the same as the copied
source file, AGPLv3.
"""

import logging

from pelican import contents, generators, signals, urlwrappers

LOGGER = logging.getLogger(__name__)


_AUTHOR_FIELDS_TO_COLLECT = (
    'author',
    'author2',
    'author3',
    'author4',
    'author5',
    'author6',
    'author7',
    'author8',
    'author9',
)
_EDITOR_FIELDS_TO_COLLECT = (
    'editor',
    'editor2',
    'editor3',
    'editor4',
    'editor5',
    'editor6',
    'editor7',
    'editor8',
    'editor9',
)


def prepare_authors_context(all_pages, canonical_authors):
    """
    Does the interesting work of compiling the authors/editors iterable for :class:`IMMAuthorList`.

    :param list all_pages: All the :class:`Page` content objects.
    :param dict canonical_authors: The AUTHOR_TO_CANONICAL dictionary from settings.
    :returns: The final object that should be attached to the context as "imm_author_list."
    :rtype: list
    """
    authors = {}
    for each_book in all_pages:
        for each_author in each_book.imm_authors:
            author_name = canonical_authors.get(each_author.name, each_author.name)

            # set up basic author information
            if author_name not in authors:
                authors[author_name] = {
                    'author name': author_name,
                    'author slug': each_author.slug,
                    'books': [],
                }

            # record book metadata
            authors[author_name]['books'].append({
                'title': each_book.title,
                'isbn13': each_book.slug,
                'is author': True,
                'is editor': False,
            })

        for each_editor in each_book.imm_editors:
            editor_name = canonical_authors.get(each_editor.name, each_editor.name)

            if editor_name not in authors:
                authors[editor_name] = {
                    'author name': editor_name,
                    'author slug': each_editor.slug,
                    'books': [],
                }

            authors[editor_name]['books'].append({
                'title': each_book.title,
                'isbn13': each_book.slug,
                'is author': False,
                'is editor': True,
            })

    # sort each author's book list
    for key, each_author in authors.items():
        authors[key]['books'] = sorted(each_author['books'], key=lambda x: x['title'])

    return sorted(list(authors.values()), key=lambda x: x['author name'])


class IMMAuthorList(generators.CachingGenerator):
    """
    Generate the "imm_authors_list" list for the templating context.
    """

    def __init__(self, *args, **kwargs):
        super(IMMAuthorList, self).__init__(*args, **kwargs)
        self.imm_authors_list = []

    def generate_context(self):
        """
        Does the generation.

        .. note:: This method is copied and modified from
            :meth:`pelican.generators.PagesGenerator.generate_context` in the Pelican library.
        """
        all_pages = []
        for each_file in self.get_files(
                self.settings['PAGE_PATHS'],
                exclude=self.settings['PAGE_EXCLUDES']):
            page = self.get_cached_data(each_file, None)
            if page is None:
                try:
                    page = self.readers.read_file(
                        base_path=self.path,
                        path=each_file,
                        content_class=contents.Page,
                        context=self.context,
                    )
                except Exception as exc:  # pylint: disable=broad-except
                    LOGGER.error(
                        'Could not process %s\n%s', each_file, exc,
                        exc_info=self.settings.get('DEBUG', False))
                    self._add_failed_source_path(each_file)
                    continue

                if not contents.is_valid_content(page, each_file):
                    self._add_failed_source_path(each_file)
                    continue

                if page.status.lower() not in ('published', 'hidden'):
                    LOGGER.error(
                        'Unknown status "%s" for file %s, skipping it.',
                        page.status, each_file)
                    self._add_failed_source_path(each_file)
                    continue

                self.cache_data(each_file, page)

            if page.status.lower() == "published":
                all_pages.append(page)
            self.add_source_path(page)

        canonical_authors = self.settings.get('AUTHOR_TO_CANONICAL', {})

        self.imm_authors_list = prepare_authors_context(all_pages, canonical_authors)
        self._update_context(('imm_authors_list',))

        self.save_cache()
        self.readers.save_cache()


def add_authors_to_page(content):
    """
    Adds the "imm_authors" and "imm_editors" fields to all :class:`Content` pages.
    """
    content.imm_authors = []
    for field in _AUTHOR_FIELDS_TO_COLLECT:
        if hasattr(content, field):
            this_field = getattr(content, field)
            if str(this_field) == content.settings.get('AUTHOR', ''):
                continue
            if isinstance(this_field, str):
                this_field = urlwrappers.Author(this_field, content.settings)
            content.imm_authors.append(this_field)

    content.imm_editors = []
    for field in _EDITOR_FIELDS_TO_COLLECT:
        if hasattr(content, field):
            content.imm_editors.append(urlwrappers.Author(getattr(content, field), content.settings))


def add_generator(nothing):  # pylint: disable=unused-argument
    """
    Adds the :class:`IMMAuthorList` generator to Pelican.
    """
    return IMMAuthorList


def register():
    """
    Connect the Pelican signals.
    """
    signals.content_object_init.connect(add_authors_to_page)
    signals.get_generators.connect(add_generator)
