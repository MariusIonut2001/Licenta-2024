import os

import torch
from transformers import AutoImageProcessor
from transformers import AutoModelForImageClassification

from backend.utils.process_predict import process_predict
from config import _settings
from ..model_base import ModelBase


class AlzheimerDetectionModel(ModelBase):
    def init(self):
        preset_model = _settings.model.split('/')[-1]
        preset_processor = _settings.model.split('/')[1]
        if preset_model not in os.listdir(_settings.models_path):
            self.model = AutoModelForImageClassification.from_pretrained(_settings.model)
            self.processor = AutoImageProcessor.from_pretrained(_settings.processor)
            self.model.save_pretrained(os.path.join(_settings.model, preset_model))
            self.processor.save_pretrained(os.path.join(_settings.processor, preset_processor))
        else:
            self.model = AutoModelForImageClassification.from_pretrained(os.path.join(_settings.model, preset_model))
            self.processor = AutoImageProcessor.from_pretrained(os.path.join(_settings.model, preset_model))

    def predict(self, img):
        inputs = self.processor(img, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits

        predicted_class_idx = logits.argmax(-1).item()

        predict = self.model.config.id2label[predicted_class_idx]

        pred = process_predict(predict)

        return pred, predict
