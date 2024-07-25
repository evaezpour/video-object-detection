import sys
import os

# Print PYTHONPATH
print("PYTHONPATH:", sys.path)

# Check if GroundingDINO is in PYTHONPATH
home = os.getcwd()
groundingdino_path = os.path.join(home, 'GroundingDINO')
if groundingdino_path in sys.path:
    print("GroundingDINO path is in PYTHONPATH")
else:
    print("GroundingDINO path is NOT in PYTHONPATH")

# Try importing GroundingDINO
try:
    from groundingdino.util.inference import Model
    print("GroundingDINO is installed correctly.")
except ImportError as e:
    print("Error importing GroundingDINO:", e)
