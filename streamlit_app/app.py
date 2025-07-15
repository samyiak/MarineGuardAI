import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Marine Animal Identifier", layout="centered")

# Ocean Theme
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to bottom, #001f3f, #003366, #004080);
        color: white;
    }
    .stButton > button {
        background-color: #00bfff;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    .stProgress > div > div {
        background-color: #00bfff !important;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    model_path = "models/marine_classifier_model.h5"
    return tf.keras.models.load_model(model_path)

model = load_model()
class_labels = ['barracuda', 'mahi_mahi', 'parrotfish', 'sailfish', 'snapper', 'whale_shark']

# Title
st.title("🌊 Marine Animal Identifier")
st.markdown("Upload a clear photo of a marine animal. The AI will identify it and show confidence levels.")

# File uploader
uploaded_file = st.file_uploader("📸 Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption="🔍 Uploaded Image", use_column_width=True)

    img_resized = img.resize((224, 224))
    img_array = image.img_to_array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    if st.button("🔎 Identify"):
        preds = model.predict(img_array)[0]
        pred_index = np.argmax(preds)
        pred_class = class_labels[pred_index]
        confidence = preds[pred_index] * 100

        st.markdown(f"### ✅ Prediction: `{pred_class.replace('_', ' ').title()}`")
        st.progress(float(confidence) / 100)
        st.markdown(f"**Confidence:** `{confidence:.2f}%`")

        # Chart
        st.markdown("#### 📊 Class Probabilities:")
        fig, ax = plt.subplots()
        ax.barh(class_labels, preds * 100, color='deepskyblue')
        ax.set_xlabel("Confidence (%)", color='white')
        ax.set_xlim(0, 100)
        ax.tick_params(colors='white')
        ax.set_facecolor('#003366')
        fig.patch.set_facecolor('#003366')
        st.pyplot(fig)

        # 🔗 Simulator link
        st.markdown(
    "<a href='https://frolicking-licorice-54f3a1.netlify.app' target='_blank'>🛡️ <button style='background-color:#00c2ff; color:white; padding:10px 20px; border:none; border-radius:10px;'>Protect This Species</button></a>",
    unsafe_allow_html=True)


    st.divider()
else:
    st.info("📥 Upload an image to get started.")

