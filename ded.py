import pandas as pd

from pathlib import Path
import PIL

from PIL import Image

# External packages
import streamlit as st


# Local Modules
import settings
import helper





# Setting page layout
st.set_page_config(
    page_title="Solar Panel Detection",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
##st.title("Solar Panel Detection")
st.markdown("<h1 style='text-align: center; color: orange;'><u>SOLAR PANEL DETECTION</u></h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("*MODEL CONFIGURATIONS*",divider='rainbow')

# Model Options
model_type = st.sidebar.radio(
    "Select Model Type", ['Detection', 'Segmentation'])

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 25, 100, 40)) / 100



DETECTION_MODEL = r'C:\Users\venkatesh.g.lv\object_detect_streamlit\Model\best.pt'
SEGMENTATION_MODEL = ''
# Selecting Detection Or Segmentation
if model_type == 'Detection':
    model_path = Path(DETECTION_MODEL)
elif model_type == 'Segmentation':
    model_path = Path(SEGMENTATION_MODEL)



# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)


SOURCES_LIST = ['IMAGE', 'VIDEO']
st.sidebar.header("*DATA SOURCE TYPE*",divider='rainbow')
source_radio = st.sidebar.radio(
    "Select Source", SOURCES_LIST)



source_img = None
# If image is selected
if source_radio == settings.IMAGE: 
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    col1, col2 = st.columns(2)


    with col1:
        try:
            if source_img is None:
                default_image_path = settings.DEFAULT_IMAGE
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image, caption="Default Image",
                         use_column_width=True)
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Uploaded Image",
                         use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None:
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image, caption='Detected Image',
                     use_column_width=True)
        else:
            if st.sidebar.button('Detect Objects'):
                res = model.predict(uploaded_image,
                                    conf=confidence
                                    )
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='Detected Image',
                         use_column_width=True)
                try:
                    with st.expander("Detection Results"):
                        for box in boxes:
                            st.write(box.data)
                except Exception as ex:
                    # st.write(ex)
                    st.write("No image is uploaded yet!")
