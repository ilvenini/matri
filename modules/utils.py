import streamlit as st
import requests

TOKEN = st.secrets["BOT_TOKEN"] # BotFather
CHAT_ID_ANDREA = st.secrets["CHAT_ID_ANDREA"]
CHAT_ID_ANNA = st.secrets["CHAT_ID_ANNA"]    

# Funzione per caricare il CSS con font personalizzati
def set_font(font_name):
    st.markdown(f"""
        <html lang="en">
        <style>
            @import url('https://fonts.googleapis.com/css2?family={font_name.replace(" ", "+")}:wght@400;700&display=swap');
            * {{
                font-family: '{font_name}', sans-serif;
            }}
            h1 {{ font-family: '{font_name}', sans-serif !important; font-size: 24px !important; }}
            h2 {{ font-family: '{font_name}', sans-serif !important; font-size: 22px !important; }}
            h3 {{ font-family: '{font_name}', sans-serif !important; font-size: 20px !important; }}
            p  {{ font-family: '{font_name}', sans-serif !important; font-size: 18px !important; }}
        </style>
    """, unsafe_allow_html=True)


# Funzione per ottenere il parametro "id" dall'URL
def get_query_params():
    query_params = st.query_params
    return query_params.get("id", None)


# Funzione per contatto
def invia_telegram(nome, messaggio):
    testo = f"📩 **Nuovo Messaggio!**\n👤 Nome: {nome}\n📝 Messaggio: {messaggio}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID_ANDREA, "text": testo, "parse_mode": "Markdown"})
    requests.post(url, data={"chat_id": CHAT_ID_ANNA, "text": testo, "parse_mode": "Markdown"}) 