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

HOMEPAGE_IMAGE_SIZES=$(shell echo {3..7}00)
IMG_SOURCE_FILE=$(THEME_DIR)/static/img/laurier_hymnal.jpg
IMG_DEST_DIR=$(OUTPUT_DIR)/static/img
JPEG_OUTPUT_FILES=$(shell echo $(IMG_DEST_DIR)/homepage-{3..7}00.jpg)
WEBP_OUTPUT_FILES=$(shell echo $(IMG_DEST_DIR)/homepage-{3..7}00.webp)


help:
	@echo 'Makefile for the Institute of Mediaeval Music website                     '
	@echo '                                                                          '


build-html:
	HOMEPAGE_IMAGE_SIZES="$(HOMEPAGE_IMAGE_SIZES)" $(PELICAN) $(INPUT_DIR) -o $(OUTPUT_DIR) -s $(CONF_FILE) $(PELICAN_OPTS)


clean:
	@rm -rf $(OUTPUT_DIR)/*


publish: clean build-html $(MAIN_CSS_FILE) images
	rm -rf $(CSS_DIR)/*.scss


netlify-publish: publish


jpeg-images: $(JPEG_OUTPUT_FILES)
$(IMG_DEST_DIR)/homepage-%.jpg: $(IMG_SOURCE_FILE)
	convert $< -resize $* $@


webp-images: $(WEBP_OUTPUT_FILES)
$(IMG_DEST_DIR)/homepage-%.webp: $(IMG_SOURCE_FILE)
	convert $< -resize $* $@


images: webp-images jpeg-images


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


build: build-html $(CSS_SOURCEMAP) images


.PHONY: html help clean publish netlify-publish build-html build-sass build-sass-debug images jpeg-images webp-images
