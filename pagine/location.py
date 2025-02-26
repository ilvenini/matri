import streamlit as st
from streamlit_folium import folium_static
import folium
from modules import utils

# Funzione per ottenere il parametro "id" dall'URL
def get_query_params():
    query_params = st.query_params
    return query_params.get("id", None)

# Pagina 1: Personalizzata per ogni utente
def app():
    utils.set_font("Delius Swash Caps")
    #st.image("savethedate.png")
    #st.write("## Matrimonio di Annamaria e Andrea")

    
    st.image("img/bersi1.png")
    
    
    user_id = get_query_params()
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

    if user_id and user_id in USER_DATA:
        st.write(USER_DATA[user_id]["text3"], unsafe_allow_html=True)
    else:
        st.write(USER_DATA['all']["text3"], unsafe_allow_html=True)

    maps_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2789.6972540616753!2d10.019785576637224!3d45.63681782190421!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x478165bef8329e71%3A0xe84fbfd81f60c13b!2sBersi%20Serlini%20Franciacorta!5e0!3m2!1sen!2sit!4v1740606188935!5m2!1sen!2sit"

    st.components.v1.iframe(maps_url, width=200, height=200)


# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "all": {"text": "Il ricevimento si terrà nell'incantevole cantina **Bersi Serlini**, situata nel cuore della Franciacorta a **Provaglio d\'Iseo** (BS).",
           "text2": "I festeggiamenti inizieranno alle ore **12.30** e dureranno fino alle ore **20.30**.",
           "text3": "Le indicazioni per raggiungerci.",},
}
