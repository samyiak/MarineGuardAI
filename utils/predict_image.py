# utils/predict_image.py

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os

# Load model
model_path = os.path.join("models", "marine_classifier_model.h5")
model = tf.keras.models.load_model(model_path)

# Define class labels (must match training order)
class_labels = ['barracuda', 'mahi_mahi', 'parrotfish', 'sailfish', 'snapper', 'whale_shark']

# Image to test
img_path = "test_images/maxresdefault.jpg"  # replace with actual image path

# Preprocess
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predict
preds = model.predict(img_array)
predicted_class = class_labels[np.argmax(preds)]
confidence = np.max(preds) * 100

print(f"✅ Predicted: {predicted_class} ({confidence:.2f}%)")
