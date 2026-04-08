import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ---------- PAGE CONFIG ---------- #

st.set_page_config(
    page_title="Potato AI Detector",
    page_icon="🥔",
    layout="centered"
)

# ---------- DARK THEME CSS ---------- #

page_style = """
<style>

[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1518977676601-b53f82aba655");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

.main-card{
background: rgba(20,20,20,0.85);
padding: 35px;
border-radius: 20px;
box-shadow: 0px 0px 25px rgba(0,255,120,0.3);
border: 1px solid rgba(255,255,255,0.1);
}

.title{
text-align:center;
font-size:48px;
font-weight:bold;
background: linear-gradient(90deg,#00ff9d,#00d4ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
text-align:center;
font-size:18px;
color:#cccccc;
}

.highlight{
color:#00ff9d;
font-weight:bold;
}

.footer{
text-align:center;
color:#888;
margin-top:40px;
}

</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# ---------- TITLE ---------- #

st.markdown('<p class="title">🥔 Potato AI Disease Detector</p>', unsafe_allow_html=True)

st.markdown(
'<p class="subtitle">Upload a <span class="highlight">Potato Leaf Image</span> and let AI detect the disease instantly</p>',
unsafe_allow_html=True
)

st.write("")

# ---------- LOAD MODEL ---------- #

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("1.keras")

model = load_model()

# ---------- CLASS LABELS ---------- #

class_names = [
    "Early Blight",
    "Late Blight",
    "Healthy"
]

IMAGE_SIZE = 256

# ---------- UI CARD ---------- #

st.markdown('<div class="main-card">', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Upload Potato Leaf Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Leaf Image", use_container_width=True)

    img = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)

    with st.spinner("🌿 AI analyzing the leaf..."):

        prediction = model.predict(img_array)

        predicted_class = class_names[np.argmax(prediction[0])]
        confidence = round(100 * np.max(prediction[0]),2)

    st.success(f"🌱 Detected Disease: **{predicted_class}**")

    st.progress(int(confidence))

    st.write(f"Confidence Level: **{confidence}%**")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ---------- #

st.markdown(
'<p class="footer">Powered by Deep Learning | Built with Streamlit</p>',
unsafe_allow_html=True
)