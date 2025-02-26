import streamlit as st


# Funzione per caricare il CSS con font personalizzati
def set_font(font_name):
    st.markdown(f"""
        <html lang="en">
        <style>
            @import url('https://fonts.googleapis.com/css2?family={font_name.replace(" ", "+")}:wght@400;700&display=swap');
            * {{
                font-family: '{font_name}', sans-serif;
            }}
            h1 {{ font-family: '{font_name}', sans-serif !important; font-size: 36px !important; }}
            h2 {{ font-family: '{font_name}', sans-serif !important; font-size: 30px !important; }}
            h3 {{ font-family: '{font_name}', sans-serif !important; font-size: 26px !important; }}
            p  {{ font-family: '{font_name}', sans-serif !important; font-size: 20px !important; }}
        </style>
    """, unsafe_allow_html=True)

