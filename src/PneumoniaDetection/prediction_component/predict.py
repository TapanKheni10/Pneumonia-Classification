from PneumoniaDetection.model_component.model import PneumoniaModel
import torchvision.transforms as transforms
from PIL import Image
import torch
from PneumoniaDetection import logger
import numpy as np

class PredictionPipeline:
    def __init__(self, img: Image.Image):
        self.img = img
        self.best_model_parameters = torch.load('models/best_model.pth', map_location=torch.device('cpu'))
        self.model = PneumoniaModel(input_shape=1, output_shape=1, hidden_units=4)
        self.transform = transforms.Compose([
            transforms.Resize((512, 512)),
            transforms.ToTensor(),
        ])

    def predict(self):
        logger.info("Loading best model parameters")
        self.model.load_state_dict(self.best_model_parameters["model_state_dict"])

        logger.info("Transforming image")
        img = self.transform(self.img).unsqueeze(dim=0)
        logger.info(f"Image shape: {img.shape}")
        logger.info(f"Image type: {img.dtype}")

        logger.info("Pneumonia detection in progress...")
        self.model.eval()

        with torch.inference_mode():
            y_logits = self.model(img).squeeze()
            y_pred_prob = torch.sigmoid(y_logits)
            prediction = torch.round(y_pred_prob)

        logger.info(f"Prediction probability: {y_pred_prob}")
        logger.info(f"Pneumonia detection completed.")

        return y_pred_prob
