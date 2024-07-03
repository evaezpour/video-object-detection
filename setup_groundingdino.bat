@echo off
set HOME=%HOMEDRIVE%%HOMEPATH%
cd %HOME%

:: Install PyTorch
echo Installing PyTorch...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

:: Clone the GroundingDINO repository if it doesn't exist
if not exist "GroundingDINO" (
    echo Cloning GroundingDINO repository...
    git clone https://github.com/IDEA-Research/GroundingDINO.git
) else (
    echo "GroundingDINO directory already exists. Skipping clone."
)

cd GroundingDINO

:: Check out the specific branch
echo Checking out the feature/more_compact_inference_api branch...
git checkout feature/more_compact_inference_api

:: Install the requirements
echo Installing GroundingDINO dependencies...
pip install -q -e .

echo "GroundingDINO setup complete."
pause