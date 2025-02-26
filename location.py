import streamlit as st
from streamlit_folium import folium_static
import folium
from utils import set_font

# Funzione per ottenere il parametro "id" dall'URL
def get_query_params():
    query_params = st.query_params
    return query_params.get("id", None)

# Pagina 1: Personalizzata per ogni utente
def app():
    set_font("Delius Swash Caps")
    #st.image("savethedate.png")
    #st.write("## Matrimonio di Annamaria e Andrea")

    
    st.image("bersi1.png")
    
    
    user_id = get_query_params()
    if user_id and user_id in USER_DATA:
        st.write(USER_DATA[user_id]["text"], unsafe_allow_html=True)
    else:
        st.write(USER_DATA['all']["text"], unsafe_allow_html=True)
    
    st.image("bersi2.png")
    
    if user_id and user_id in USER_DATA:
        st.write(USER_DATA[user_id]["text2"], unsafe_allow_html=True)
    else:
        st.write(USER_DATA['all']["text2"], unsafe_allow_html=True)
  
    st.image("bersi3.png")

# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "all": {"text": "Il ricevimento si terrà nell'incantevole cantina **Bersi Serlini**, situata nel cuore della Franciacorta a **Provaglio d\'Iseo** (BS).",
           "text2": "I festeggiamenti inizieranno alle ore **12.30** e dureranno fino alle ore **20.30**.",},
}
