# Book Entries
Book entries consist of two main parts, the "front matter" and the "content". The "front matter", also known as "metadata", is written in YAML, while the "content", also known as "description", can consist of plain text, Markdown, or raw HTML. The book entries are classified into subfolders based on series and will gain the subfolder name as `series` metadata unless it's otherwise specified in the book entries front matter. The files are generally named using their ISBN number to ensure uniqueness.

```
---
title: A book
author: Author, Some
year: 2025
---
This is some content
```

## Front Matter
The front matter appears at the top of the file, is wrapped in `---` and provides the metadata for the book. Refer to `metadata_fields.md` for a list of fields supported for book entries.

In addition to the fields listed in `metadata_fields.md` you can also specify `layout: book` to have the site pick up any file as if it was a book, regardless of where it's found in the site. Any file under `books/` will inherit the book layout (which describes how the page should look) so in most cases it should be unnecessary to specify.

## Content
The rest of the file below the front matter, is the page content. This will be added as the description on the book page.