# Metadata Fields for Book Entries

## Authors
### author
Name of the first/only author of the book. In the format "Last name, First name"
```yaml
author: Author, First
```
### author[2-99]
Additional authors of the book if any. Follows the same format as the `author` field above.
```yaml
author2: Author, Second
author3: Author, Third
author99: Author, Ninty-ninth
```
### authors
List of the people who wrote the book. Equivalent to the `author` field plus any number of `author2` to `author99` fields. Need to prefix each line with a `-` and the order of the names **is** significant.
```yaml
authors:
- Author, First
- Author, Second
- Author, Third
```

### author_names (Auto Generated)
Collected list of all of the above author names. Used for rendering the authors on the book page. **DO NOT INCLUDE MANUALLY**

## Editors
### editor
Name of the first/only editor of the book. In the format "Last name, First name"
```yaml
editor: Editor, First
```
### editor[2-99]
Additional editors of the book if any. Follows the same format as the `editor` field above.
```yaml
editor2: Editor, Second
editor3: Editor, Third
editor99: Editor, Ninty-ninth
```
### editors
List of the people who edited the book. Equivalent to the `editor` field plus any number of `editor2` to `editor99` fields. Need to prefix each line with a `-` and the order of the names **is** significant.
```yaml
editors:
- Editor, First
- Editor, Second
- Editor, Third
```

### editor_names (Auto Generated)
Collected list of all of the above editor names. Used for rendering the editors on the book page. **DO NOT INCLUDE MANUALLY**

## Volume
### volume
Main volume number. Often expressed in roman numerals
```yaml
volume: XVII
```
### volume_part
Part of a volume. Combined with `volume` field to created the full volume number displayed to users. Often expressed in digits
```yaml
volume_part: 2
```
When combined with `volume` above the expected output would be `XVII/2`

## Prices
### price
Price of the book in euros. Do not include the euro sign
```yaml
price: 50
```

## ISBN Numbers
### isbn10
Old ISBN number printed in the older books. Was the standard before January 1st 2007
```yaml
isbn10: 0-931902-54-1
```
### isbn13
ISBN number printed in newer books. Standard since January 1st 2007
```
isbn13: 978-0-931902-54-3
```

## Pages
### pages
Number of pages in the book, entered without units
```yaml
pages: 10
```
### plates
Number of plates in the book. Could be folios ff. or pages pp. but entered without units
```yaml
plates: 456
```

## Publication Info
### year
Year of publication
```yaml
year: 2025
```
### place
Place of publication
```yaml
place: Ottawa
```
### publisher
Who published the book. Most often this is IMM
```yaml
publisher: IMM
```

## Book Info
### size
Size of the book in centimeters, entered without units
```yaml
size: 23
```
### title
Title of the book. **MUST** be quoted if the title contains a colon to avoid parsing issues
```yaml
title: Some title
```
```yaml
title: "CANTUS: Some Title"
```
### series
What series the book belongs to. **May** be inferred based on file location but can be overriden here. This determines what series page the book is listed on.
```yaml
series: studies
```
A file located in `books/studies/` will have `series: studies` added automatically if the series is not otherwise specified.
### corrigenda
Corrections made to the book. Sometimes an explanation or information, and sometimes replacement pages to download.
```yaml
corrigenda: The ISBN number is printed wrong
```

## Open Access
### pdf_url
URL of the open access PDF. Presence of this metadata will add the book to the "Open Access" list, and will also include a link to the pdf on the book page. The PDF **MUST** be publicly accessible for users to be able to view it