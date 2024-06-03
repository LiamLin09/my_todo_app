import streamlit as st
from PIL import Image

camera_image = st.camera_input('Camera')

if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)

    # convert the pillow image to grayscale
    gray_img = img.convert('L')

    # render the grayscale image on the webpage
    st.image(gray_img)