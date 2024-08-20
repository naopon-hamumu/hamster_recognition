import cv2
import streamlit as st
from PIL import Image
from ultralytics import YOLO


def app():
    st.title(":hamster:み具合アプリ")
    st.subheader("写真のハムスター度を調べます。")
    model = YOLO('yolov8n.pt')
    model = YOLO('last.pt')

    with st.form("my_form"):
        uploaded_image = st.file_uploader("画像を選択してください", type=["jpg", "jpeg", "png"])
        st.form_submit_button(label='Submit')

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="元の画像", use_column_width=True)
        results = model(image, classes=0)

        annotated_image = results[0].plot()
        annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
        annotated_image_pil = Image.fromarray(annotated_image_rgb)
        st.image(annotated_image_pil, caption="はむみ度", use_column_width=True)

if __name__ == "__main__":
    app()
