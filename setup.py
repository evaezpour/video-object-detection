from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="object_detection_package",
    version="0.1.0",
    author="evaezpour",
    author_email="your.email@example.com",
    description="A package for performing object detection in videos using a text prompt with GroundingDINO.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evaezpour/video_object_detection_package",
    packages=find_packages(),
    install_requires=[
        "torch>=1.7.1",
        "torchvision>=0.8.2",
        "torchaudio>=0.7.2",
        "opencv-python>=4.5.1.48",
        "requests>=2.25.1",
        "supervision",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
