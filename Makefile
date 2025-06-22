# Makefile for CourseClicker

PYTHON := python
ENTRY := src/courseclicker/main.py
ICON := courseclicker.ico
APP := courseclicker

.PHONY: build clean run test

build:
	$(PYTHON) build.py

clean:
	rm -rf build dist __pycache__ *.spec .pytest_cache

run:
	$(PYTHON) $(ENTRY)

test:
	pytest