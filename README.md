The Institute of Mediaeval Music Website
===================================
The website uses Jekyll and deploys to GitHub Pages using GitHub actions

## Important folders/files
### For Non-technical users
- books/
	- Contains information on the books shown in the site
- authors/
	- Contains any overridden author pages
- \_data/
	- Contains configuration options safely stored away from any code
- index.md
	- Contains content for the home page
- ordering.md
	- Contains content for the ordering page
### For Developers
In addition to the above folders
- .github/workflows
	- Contains GitHub Actions workflows
- \_plugins
	- Contains custom ruby plugins for generating site content
- \_config.yml
	- Overall Jekyll site configuration
- \_layouts
	- HTML Markup for how to render content
	- base.html defines base layout, inherited by other pages
	- default.html defines layout used by pages unless another layout is specified
- authors.html
	- Contains logic for rendering the authors list page.
	- Content generated based off authors/editors listed in books
- online.html
	- Contains logic for rendering the online access book list page.
	- Content generated based off of books with `pdf_url` front matter
- series.html
	- Contains logic for rendering the series list page.
	- Content generated based off of the values found in `series` front matter of books.
	- `series` front matter may be implied by sub folder for books under `books/`
- titles.html
	- Contains logic for rendering the titles list page.
	- Content generated based off of the titles of books
- manifest.json
	- PWA Manifest
	- Defines where to find icons if added to home screen of android device
- Gemfile / Gemfile.lock
	- Ruby bundler files
- assets
	- Website assets
	- img/original contains unscaled images
		- scaled versions created by GitHub Actions automatically
- apple-touch-icon.png
	- Image used by apple devices for icon on home screen
	- Added to support the site being added to the home screen
- \_sass
	- SCSS files for styling the site
- \_includes
	- Reusable parts of the site (ie. navbar or quick links)
	- Included in other layouts

## Set Up
1. Install Ruby
	- Should match version specified in `.github/workflows/deploy.yml` to ensure compatibility
2. Clone `https://github.com/medieval-music/website.git`
3. Run `bundle install`

To build the site run `bundle exec jekyll build`  
For local development run `bundle exec jekyll serve --livereload`  

The site will run locally on port 4000 and be accessable from `localhost:4000` OR from other devices on the local network (assuming firewall rules don't block it). This can make it easier to locally test on mobile.