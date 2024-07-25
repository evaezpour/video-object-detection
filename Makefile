# Makefile for Python project

# Variables
PYTHON := python3
PIP := $(PYTHON) -m pip
i :=
o :=
t :=

# Default target
.PHONY: all
all: install test

# Install dependencies (including GroundingDINO setup)
.PHONY: install
install:
	@echo "Installing system dependencies..."
	sudo apt-get update
	sudo apt-get install -y libgl1-mesa-glx
	@echo "System dependencies installed."
	@echo "Installing Python dependencies..."
	$(PIP) install --prefer-binary -v -r requirements.txt
	@echo "Dependencies installed."
	@echo "Setting up GroundingDINO model..."
	@if [ ! -d "GroundingDINO" ]; then \
		git clone https://github.com/IDEA-Research/GroundingDINO.git; \
	fi
	@cd GroundingDINO && $(PYTHON) -m pip install . -v
	@echo "GroundingDINO setup complete."
	export PYTHONPATH=$(PYTHONPATH):$(shell pwd)/GroundingDINO


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


.PHONY: run
run:
	# Run the main script
	ifndef i
		$(error input video file path is required)
	endif

	ifndef o
		$(error output video directory is required)
	endif

	ifndef t
		$(error text prompt is required)
	endif

	$(PYTHON) -m object_detector -i="$(i)" -o="$(o)" -t="$(t)"

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install : Install dependencies and set up GroundingDINO model"
	#@echo "  test    : Run tests"
	@echo "  clean   : Clean up generated files"
	@echo "  run     : Run the main script"
	@echo "  help    : Show this help message"
