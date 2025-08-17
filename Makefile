# Makefile for DHUM25A43 Course Slides

.PHONY: html lint pretty watch

lint:
	npx markdownlint slides/**/*.md

pretty:
	npx prettier --write slides/**/*.md

html: pretty
	npx marp --html --allow-local-files --theme slides/themes/minimal-dark.css --input-dir slides/ --output slides/


watch:
	find slides -name "*.md" | entr -s 'make html'

dev: watch