# utils/preprocess.py

import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split

# Paths
IMAGE_SIZE = (224, 224)
DATA_DIR = os.path.join("data", "raw_images")
CATEGORIES = ['barracuda', 'mahi_mahi', 'parrotfish', 'sailfish', 'snapper', 'whale_shark']

print("📦 Categories:", CATEGORIES)

data, labels = [], []

for label, category in enumerate(CATEGORIES):
    folder = os.path.join(DATA_DIR, category)
    if not os.path.exists(folder):
        print(f"⚠️ Folder missing: {folder}")
        continue
    for img_file in os.listdir(folder):
        img_path = os.path.join(folder, img_file)
        try:
            img = load_img(img_path, target_size=IMAGE_SIZE)
            img_array = img_to_array(img)
            data.append(img_array)
            labels.append(label)
        except Exception as e:
            print(f"❌ Failed to load {img_file}: {e}")

X = np.array(data, dtype="float32") / 255.0
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Save to processed folder
processed_dir = os.path.join("data", "processed")
os.makedirs(processed_dir, exist_ok=True)

np.save(os.path.join(processed_dir, "X_train.npy"), X_train)
np.save(os.path.join(processed_dir, "X_test.npy"), X_test)
np.save(os.path.join(processed_dir, "y_train.npy"), y_train)
np.save(os.path.join(processed_dir, "y_test.npy"), y_test)

print("✅ Preprocessing complete. Data saved.")
