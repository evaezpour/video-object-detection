# Makefile for Python project

# Variables
PYTHON := python3
PIP := $(PYTHON) -m pip
BAT := cmd /c setup_groundingdino.bat  # Command to run .bat script (Windows)

# Default target
.PHONY: all
all: install test

# Install dependencies (including GroundingDINO setup)
.PHONY: install
install:
	$(PIP) install -v -r requirements.txt
	@echo "Dependencies installed."
	@echo "Setting up GroundingDINO model..."
	$(BAT)
	@echo "GroundingDINO setup complete."

# Run tests
#.PHONY: test
#test:
#    $(PYTHON) -m pytest tests/
#    @echo "Tests complete."

# Clean up generated files
.PHONY: clean
clean:
	rm -rf build/ dist/ *.egg-info/
	@echo "Cleaned up."

# Run the main script
.PHONY: run
run:
	$(PYTHON) path/to/main_script.py

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install : Install dependencies and set up GroundingDINO model"
	@echo "  test    : Run tests"
	@echo "  clean   : Clean up generated files"
	@echo "  run     : Run the main script"
	@echo "  help    : Show this help message"
