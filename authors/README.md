# Author Pages
An author page is automatically generated for every author and editor found in the book entries. Creating an file here with the same name as an author/editor will override content of the generated author page.

## How to override the author page for an author
Follow the following steps to override the generated author page for a given author
1. Go to the website and find the page for the author who's page you'd like to override
2. The URL bar at the top will end with something along the lines of `authors/last-first.html`
3. Create an Markdown file in the `authors/` directory with the same name as you observed in the URL
	- For the above example `authors/last-first.html`, create the file `last-first.md` in the `authors/` directory
4. This will prevent the site from automatically generating an author page for that author
5. Specify the authors name as the `title` in the page's front matter, and provide what ever content you'd want to display about the author

For the example above, the following will override the author page. Assume the file is named `last-first.md` as outlined in the steps above.
```
---
title: Last, First
---
Some content to show, such as author's biography
```

## Unoverridable content
The list of books the author has authored or edited **CANNOT** be overridden. the `books_authored` and `books_edited` metadata will be replaced at build time with the computed list of books that have the author listed as an author or editor respectively. Any values listed in the front matter of the author page will be **ignored**