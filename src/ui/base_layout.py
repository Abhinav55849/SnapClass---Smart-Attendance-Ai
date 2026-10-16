import streamlit as st


def style_background_home():

    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #667EEA 0%, #764BA2 50%, #F093FB 100%) !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #FFFFFF !important;
                padding: 1.5rem !important;
                border-radius: 4rem !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>
            .stApp {
                background: #D8CFF0 !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Top Bar of streamlit */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 0.5rem !important;
            padding-bottom: 1rem !important;
        }

        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2.4rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 1.6rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
        }

        .stApp div[data-testid="stColumn"] h2 {
            color: #2E2E2E !important;
        }        
        h3, h4, p {
            font-family: 'Outfit', sans-serif;
        }

        button {
            border-radius: 1.5rem !important;
            background-color: #FF4500 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background-color: #FF4500 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background-color: black !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button:hover {
            transform: scale(1.05);
        }
        </style>
    """, unsafe_allow_html=True)