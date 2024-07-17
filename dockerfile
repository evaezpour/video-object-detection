# Use a pre-built PyTorch image as a parent image
FROM pytorch/pytorch:2.3.1-cuda11.8-cudnn8-runtime

# Set environment variables
ENV HOME /root
ENV GROUNDINGDINO_DIR /app/GroundingDINO

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone the GroundingDINO repository and install its dependencies
RUN git clone https://github.com/IDEA-Research/GroundingDINO.git $GROUNDINGDINO_DIR && \
    cd $GROUNDINGDINO_DIR && \
    pip install -v -e .

# Set the PYTHONPATH to include the GroundingDINO directory
#ENV PYTHONPATH="${PYTHONPATH}:${GROUNDINGDINO_DIR}"
ENV PYTHONPATH=$PYTHONPATH:$GROUNDINGDINO_DIR:$GROUNDINGDINO_DIR/groundingdino

# Copy only requirements.txt to leverage caching
COPY requirements.txt /app/requirements.txt

# Install the rest of the dependencies
RUN pip install -r /app/requirements.txt

# Copy the rest of the application
COPY . /app

# Install the package
RUN pip install .

# Set the entry point to your Python script
ENTRYPOINT ["python", "object_detector/__main__.py"]
