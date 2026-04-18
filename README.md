# 🥔 Potato Leaf Disease Detection using Deep Learning

A **Deep Learning based web application** that detects potato leaf diseases from images using a trained **Convolutional Neural Network (CNN)** model.
The application is built with **TensorFlow/Keras** and deployed using **Streamlit** for an interactive web interface.

<img width="2559" height="1274" alt="Screenshot 2026-04-08 122011" src="https://github.com/user-attachments/assets/01b9d84b-bcc0-47c8-a38c-2efacd494ac4" />

---

## 📌 Project Overview

Plant diseases significantly reduce agricultural productivity. Early detection of diseases in potato plants can help farmers take preventive actions and reduce crop loss.

This project uses **Deep Learning and Computer Vision** to automatically classify potato leaf images into disease categories.

The model predicts whether a leaf is:

* 🌿 **Healthy**
* 🍂 **Early Blight**
* 🦠 **Late Blight**

Users can upload an image of a potato leaf and instantly receive the predicted disease with a confidence score.

---

## 🚀 Features

* Upload potato leaf images
* AI-powered disease prediction
* Confidence score display
* Modern **dark-themed Streamlit UI**
* Image preview before prediction
* Simple and user-friendly interface

---

## 🧠 Model Information

The model is trained using a **Convolutional Neural Network (CNN)** on a dataset of potato leaf images.

Model file:

```
1.keras
```

Classes predicted by the model:

```
Early Blight
Late Blight
Healthy
```

---

## 🖥 Web Application

The application interface is built using **Streamlit**.

Users can:

1. Upload a potato leaf image
2. The model processes the image
3. The predicted disease and confidence score are displayed

---

## 📂 Project Structure

```
potato-disease-detector
│
├── app.py              # Streamlit application
├── 1.keras             # Trained deep learning model
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Afsal0808/potato-disease-detector.git
```

Move into the project folder:

```bash
cd potato-disease-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Open the browser at:

```
http://localhost:8501
```

Upload a potato leaf image to detect the disease.

---

## 🛠 Technologies Used

* Python
* TensorFlow / Keras
* Streamlit
* NumPy
* Pillow
* Deep Learning
* Computer Vision

---

## 📸 Example Prediction

Input: Potato leaf image

Output:

```
Prediction: Late Blight
Confidence: 97%
```

---

## 🌱 Future Improvements

* Grad-CAM visualization to highlight infected regions
* Mobile camera capture feature
* Disease treatment recommendations
* Model performance dashboard
* Cloud deployment

---

## 👨‍💻 Author

**Afsal**

Machine Learning Enthusiast | AI Developer

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**.
