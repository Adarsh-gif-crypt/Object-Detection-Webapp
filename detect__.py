import os
import streamlit as st

st.set_page_config(layout='wide',initial_sidebar_state='expanded')

titles0, title, titles1 = st.columns((1.6,6,0.5))
title.title('Object Detection')

st.sidebar.subheader('Select the type of input')
selectbox = st.sidebar.selectbox('',('Still Picture','Video','Webcam'))

if selectbox=='Still Picture' :
    st.markdown("""### Please enter the path of the picture""")
    filepath1 = st.text_input('Enter File Path',placeholder='File Path')
    raw_filepath = r'{}'.format(filepath1)
    if st.button('Detect'):
        stream = os.popen(f'python detect.py --source ./{raw_filepath}')
        output = stream.read()
        if output is not None:
            st.write(output)

if selectbox=='Video':
    st.markdown("""### Please enter the path of the video""")
    filepath1 = st.text_input('Enter File Path',placeholder='File Path')
    raw_filepath = r'{}'.format(filepath1)
    if st.button('Detect'):
        stream = os.popen(f'python detect.py --source ./{raw_filepath}')
        output = stream.read()
        if output is not None:
            st.write(output)


if selectbox=='Webcam':
    st.markdown("""### Some controls for the WebCam Window
    - Q - Quit
    - A and D - Toggle between multiple WebCam inputs""")
    if st.button('Open Webcam and Detect'):
        stream = os.popen(f'python detect.py --source 0')
        output = stream.read()
        if output is not None:
            st.write(output)