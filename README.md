# Object Detection Package

This package provides functionalities for performing object detection in videos using a text prompt with the GroundingDINO model.

## Table of Contents

1. [Installation](#installation)
2. [Docker Setup](#docker-setup)
3. [Makefile](#makefile)
4. [Jupyter Notebooks](#jupyter-notebooks)
5. [Usage](#usage)
6. [Demo](#demo)


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
 
   - Install the dependencies:

     ```sh
     pip install -q -e .
     ```

2. **Automated Installation using `setup_groundingdino.bat` for windows:**

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

After setting up GroundingDINO, you can install the video object detection package. Navigate to the directory containing `setup.py` and run:

```sh
pip install .
```

## Docker Setup
To run the project in Docker, you need to build and run the Docker container:

Navigate to the video_object_detection directory and run the following command:

```sh
docker build -t object-detection-project .
```
To run the image:
```sh
docker run --rm -v $(pwd)/input_video:/app/video_object_detection/Demo/input_video -v $(pwd)/output_video:/app/video_object_detection/Demo/output_video video-object-detection -i /app/video_object_detection/object_detector/input_video/street_trim.mp4 -o /app/video_object_detection/object_detector/output_video -t "all cars"
```

## Makefile
The Makefile automates common tasks.

To use the Makefile, run:
```sh
make install #to install package and GroundingDINO
make run i="demo/input_video/street_trim.mp4" o="demo/output_video/" t="men" #to run the package
make clean #to clean up generated files"
make help #to show the help message 
```

## Usage
Demo files are included in the demo directory:

demo/input_video/: Contains sample video files for testing.
demo/output_video/: Directory where processed videos will be saved.

To test the object detection, use one of the sample videos from input_video and run the inference_on_a_video.py file.





