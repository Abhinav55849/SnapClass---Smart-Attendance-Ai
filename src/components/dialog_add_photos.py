import streamlit as st
from PIL import Image


@st.dialog("Capture or upload photos")
def add_photos_dialog():
    st.write('Add classroom photos to scan for attendance')

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    if 'widget_counter' not in st.session_state:
        st.session_state.widget_counter = 0

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else "tertiary"
        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'
            st.rerun(scope="fragment")

    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else "tertiary"
        if st.button('Upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'
            st.rerun(scope="fragment")

    n = st.session_state.widget_counter

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Snapshot', key=f'dialog_cam_{n}')
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.session_state.widget_counter += 1 
            st.toast('Photo Captured')
            st.rerun(scope="fragment")

    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader(
            'Choose image files',
            type=['jpg', 'png', 'jpeg'],
            accept_multiple_files=True,
            key=f'dialog_upload_{n}'
        )
        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.session_state.widget_counter += 1
            st.toast('Photos added successfully!')
            st.rerun(scope="fragment")

    st.divider()
    st.caption(f"{len(st.session_state.attendance_images)} photo(s) added")
    if st.button('Done', type='primary', width='stretch'):
        st.rerun()