# Object Detection Package

This package provides functionalities for performing object detection in videos using a text prompt with the GroundingDINO model.

## Installation

### Prerequisites

Before installing the package, ensure that you have Python 3.7+, Git, and pip installed on your system.

### GroundingDINO Model Installation

To use the GroundingDINO model, you need to clone the repository and install the necessary dependencies. You have two options for this:

1. **Manual Installation:**

   - Clone the GroundingDINO repository:

     ```sh
     git clone https://github.com/IDEA-Research/GroundingDINO.git
     ```

   - Navigate to the GroundingDINO directory:

     ```sh
     cd GroundingDINO
     ```

   - Check out the specific branch:

     ```sh
     git checkout feature/more_compact_inference_api
     ```

   - Install the dependencies:

     ```sh
     pip install -q -e .
     ```

2. **Automated Installation using `setup_groundingdino.bat`:**

   - Ensure the batch script `setup_groundingdino.bat` is in your project directory:
   - Open Command Prompt and navigate to the directory containing `setup_groundingdino.bat`:

     ```sh
     cd C:\path\to\your\project
     ```

   - Run the script:

     ```sh
     .\setup_groundingdino.bat
     ```

### Package Installation

After setting up GroundingDINO, you can install the object detection package. Navigate to the directory containing `setup.py` and run:

```sh
pip install .
