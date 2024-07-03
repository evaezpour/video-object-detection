# Define variables
PYTHON := python
PIP := pip
GIT := git
CD := cd

# Define directories
HOME_DIR := $(HOME)
GROUNDINGDINO_DIR := $(HOME_DIR)/GroundingDINO
PROJECT_DIR := $(CURDIR)

# Define commands
SETUP_GROUNDINGDINO := setup_groundingdino.bat

# Targets
.PHONY: all install_groundingdino install_package install_dependencies test clean

all: install_groundingdino install_package

# Target to set up GroundingDINO
install_groundingdino:
	@if [ ! -d "$(GROUNDINGDINO_DIR)" ]; then \
		echo "Cloning GroundingDINO repository..."; \
		$(GIT) clone https://github.com/IDEA-Research/GroundingDINO.git $(GROUNDINGDINO_DIR); \
	else \
		echo "GroundingDINO directory already exists. Skipping clone."; \
	fi
	$(CD) $(GROUNDINGDINO_DIR) && $(GIT) checkout feature/more_compact_inference_api
	$(CD) $(GROUNDINGDINO_DIR) && $(PIP) install -q -e .

# Target to install the package
install_package:
	$(PIP) install .

# Target to install dependencies
install_dependencies:
	$(PIP) install -r requirements.txt

# Target to clean up
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

# Target to run the example script
run_example:
	$(PYTHON) examples/process_video_example.py
