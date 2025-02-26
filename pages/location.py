import streamlit as st
from modules import utils

# Pagina 1: Personalizzata per ogni utente

utils.set_font("Delius Swash Caps")
#st.image("savethedate.png")
#st.write("## Matrimonio di Annamaria e Andrea")

st.image("img/bersi1.png")

# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "all": {"text": "Il ricevimento si terrà nell'incantevole cantina **Bersi Serlini**, situata nel cuore della Franciacorta a **Provaglio d\'Iseo** (BS).",
           "text2": "I festeggiamenti inizieranno alle ore **12.30** e dureranno fino alle ore **20.30**.",},
}


user_id = utils.get_query_params()
if user_id and user_id in USER_DATA:
    st.write(USER_DATA[user_id]["text"], unsafe_allow_html=True)
else:
    st.write(USER_DATA['all']["text"], unsafe_allow_html=True)

st.image("img/bersi2.png")

if user_id and user_id in USER_DATA:
    st.write(USER_DATA[user_id]["text2"], unsafe_allow_html=True)
else:
    st.write(USER_DATA['all']["text2"], unsafe_allow_html=True)

st.image("img/bersi3.png")
