PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py
IMGDIR=$(OUTPUTDIR)/static/img


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make images                         generate optimzed images in output '
	@echo '   make publish                        generate using production settings '
	@ehco '   make netlify-publish                build everything from scratch      '
	@echo '   make update-submodules              runs "git submodule update"        '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

netlify-publish: update-submodule publish images

update-submodule:
	git submodule update

images:
	convert $(IMGDIR)/laurier_hymnal.jpg -resize 200 $(IMGDIR)/homepage-200px.jpg
	convert $(IMGDIR)/laurier_hymnal.jpg -resize 300 $(IMGDIR)/homepage-300px.jpg
	convert $(IMGDIR)/laurier_hymnal.jpg -resize 400 $(IMGDIR)/homepage-400px.jpg
	convert $(IMGDIR)/laurier_hymnal.jpg -resize 500 $(IMGDIR)/homepage-500px.jpg
	convert $(IMGDIR)/laurier_hymnal.jpg -resize 200 $(IMGDIR)/homepage-200px.webp
	convert $(IMGDIR)/laurier_hymnal.jpg -resize 300 $(IMGDIR)/homepage-300px.webp
	convert $(IMGDIR)/laurier_hymnal.jpg -resize 400 $(IMGDIR)/homepage-400px.webp
	convert $(IMGDIR)/laurier_hymnal.jpg -resize 500 $(IMGDIR)/homepage-500px.webp

.PHONY: html help clean regenerate serve serve-global devserver stopserver publish images update-submodule
