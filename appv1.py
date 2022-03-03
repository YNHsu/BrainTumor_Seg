import streamlit as st
import numpy as np
from PIL import Image
import time



# App Title
st.title("Brain tumor segmentation APP")

st.markdown(unsafe_allow_html=True, body="<p>This is a basic app built with Streamlit.")
                                        


# =============================================================================
# img = st.file_uploader(label='Load a CT brain image', type=['png','jpg','jpeg'], key='CT', accept_multiple_files=False)
# basename = img.name
# =============================================================================

imgname = st.selectbox('Select the CT image', (None, 'CTbrain_1.png','CTbrain_2.png','CTbrain_3.png','CTbrain_4.png','CTbrain_5.png','CTbrain_6.png','CTbrain_7.png','CTbrain_8.png'))


if imgname is not None:
    img = Image.open(f'CTimage/{imgname}')
    st.subheader('CT image')
    st.image(img, width=340)
    
    pred = st.button('Predict')
    if pred is True:
        st.text('Predicting...')
        col1, col2 = st.columns(2)
        
        time.sleep(1)
        Segment = Image.open(f'CToverlay/{imgname}')
        col1.subheader('Segmentation')
        col1.image(Segment, use_column_width=True, caption='Ground Truth(Red line)\nPrediction(Blue line)')
        
        time.sleep(1)
        GradCAM = Image.open(f'GradCAM/{imgname}')
        col2.subheader('GradCAM')
        col2.image(GradCAM, use_column_width=True)
        



    