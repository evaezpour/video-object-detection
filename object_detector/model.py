import os
import requests
from groundingdino.util.inference import Model


def download_weights(weights_path, url):

    os.makedirs(os.path.dirname(weights_path), exist_ok=True)
    response = requests.get(url)
    with open(weights_path, "wb") as f:
        f.write(response.content)


def get_model_paths():

    home = os.getcwd()

    config_path = os.path.join(home, "GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py")
    print("----------this is it --------------------------------")
    print(home)
    print(config_path)
    print("----------this is it --------------------------------")
    weights_path = os.path.join(home, "GroundingDINO/groundingdino/weights/groundingdino_swint_ogc.pth")
    if not os.path.exists(weights_path):
        url = "https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth"
        download_weights(weights_path, url)

    return config_path, weights_path


def load_grounding_dino_model():

    config_path, weights_path = get_model_paths()
    return Model(model_config_path=config_path, model_checkpoint_path=weights_path)
