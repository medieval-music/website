PY?=python3
PELICAN?=pelican
PELICAN_OPTS=

BASE_DIR=$(CURDIR)
INPUT_DIR=$(BASE_DIR)/content
OUTPUT_DIR=$(BASE_DIR)/output
CONF_FILE=$(BASE_DIR)/pelicanconf.py

THEME_DIR=$(BASE_DIR)/theme
SASS_DIR=$(THEME_DIR)/static/css
MAIN_SASS_FILE=$(SASS_DIR)/main.scss
CSS_DIR=$(OUTPUT_DIR)/static/css
MAIN_CSS_FILE=$(CSS_DIR)/main.css
CSS_SOURCEMAP=$(CSS_DIR)/main.css.map


help:
	@echo 'Makefile for the Institute of Mediaeval Music website                     '
	@echo '                                                                          '


build-html:
	$(PELICAN) $(INPUT_DIR) -o $(OUTPUT_DIR) -s $(CONF_FILE) $(PELICAN_OPTS)


clean:
	@rm -rf $(OUTPUT_DIR)/*


publish: clean build-html $(MAIN_CSS_FILE)
	rm -rf $(CSS_DIR)/*.scss


netlify-publish: clean publish $(MAIN_CSS_FILE) images


images:
	cd output && bash compress_images.html


build-sass: $(MAIN_CSS_FILE)
$(MAIN_CSS_FILE): $(SASS_DIR)/*.scss
	@rm -rf $(CSS_DIR)/*
	@mkdir -p $(CSS_DIR)
	sassc --output-style=compressed $(MAIN_SASS_FILE) $(MAIN_CSS_FILE)


build-sass-debug: $(CSS_SOURCEMAP)
$(CSS_SOURCEMAP): $(SASS_DIR)/*.scss
	@rm -rf $(CSS_DIR)/*
	@mkdir -p $(CSS_DIR)
	sassc --output-style=expanded --sourcemap $(MAIN_SASS_FILE) $(MAIN_CSS_FILE)


build: build-html $(CSS_SOURCEMAP)


.PHONY: html help clean publish netlify-publish images build-html build-sass build-sass-debug
