# Object Detection Package

The "video_object_detection" project is designed to perform object detection in video files, utilizing text prompts to guide the detection process. The key components and functionalities include:

- Text Prompt-Based Detection: The project uses text prompts to specify the types of objects to detect in the video. 

- Video Processing Pipeline: The system processes video files frame by frame. Each frame is analyzed to identify objects matching the text prompt, and annotations are added to the frames.

- Object Detection with GroundingDINO: GroundingDINO model is employed to handle the core object detection tasks. It utilizes text prompts to ground object detection.

- Annotation and Output: Detected objects are annotated with bounding boxes and labels. These annotations are visualized in the output video, making it easier to verify and interpret the results.

- Integration and Configuration: The project includes setup scripts and configuration files to streamline the installation and configuration of dependencies, including GroundingDINO.

## Table of Contents

1. [Installation](#installation)
2. [Docker Setup](#docker-setup)
3. [Makefile](#makefile)
4. [Jupyter Notebooks](#jupyter-notebooks)
5. [Usage](#usage)
6. [Demo](#demo)


## Installation

For installation, you need to install the video_object_detection package and the GroundingDINO model. The steps are explained as follows.

### Prerequisites

Before installing the package, ensure that you have Python 3.7+, Git, and pip installed on your system.

### Package Installation:

You can install the video object detection package. Navigate to the directory containing `setup.py` and run:

```sh
pip install .
```

### GroundingDINO Model Installation:

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
   
   - Add GroundingDINO to Python path 

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

   - Add GroundingDINO to Python path
   

## Docker Setup
To run the project in Docker, you need to build and run the Docker container:

Navigate to the video_object_detection directory and run the following command:

```sh
docker build -t video_object_detection .
```
To run the image:
```sh
docker run --rm -v $(pwd)/input_video:/app/video_object_detection/Demo/input_video -v $(pwd)/output_video:/app/video_object_detection/Demo/output_video video-object-detection -i /app/video_object_detection/object_detector/Demo/input_video/street_trim.mp4 -o /app/video_object_detection/object_detector/Demo/output_video -t "all cars"
```

## Makefile
The Makefile automates common tasks.

To use the Makefile, run:
```sh
make install #to install the package and GroundingDINO
make run i="demo/input_video/street_trim.mp4" o="demo/output_video/" t="men" #to run the package
make clean #to clean up generated files"
make help #to show the help message 
```
## Jupyter Notebooks
There is a Jupyter Notebook in the "notebooks" directory that can be used to run the package.  

## Usage
Demo files are included in the demo directory:

- demo/input_video/: Contains sample video files for testing.
- demo/output_video/: Directory where processed videos will be saved.

To test the object detection, use one of the sample videos from input_video and run the inference_on_a_video.py file.





