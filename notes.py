import streamlit as st
from utils import set_font
    

# Pagina 1: Personalizzata per ogni utente
def app():
    set_font("Delius Swash Caps")


# Funzione per ottenere il parametro "id" dall'URL
def get_query_params():
    query_params = st.query_params
    return query_params.get("id", None)

# Pagina 1: Personalizzata per ogni utente
def app():
    set_font("Delius Swash Caps")
    #st.write("## Matrimonio di Annamaria e Andrea")

    
    user_id = get_query_params()
    if user_id and user_id in USER_DATA:
        st.write(USER_DATA[user_id]["text"], unsafe_allow_html=True)
    else:
        st.write(USER_DATA['all']["text"], unsafe_allow_html=True)

    
# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "all": {"text": "Per permetterci di organizzare al meglio la festa, vi chiediamo di **confermare la vostra presenza entro il 15 maggio**!<br><br>\
    Se avete **intolleranze, allergie alimentari o seguite una dieta vegetariana**, vi preghiamo di farcelo sapere, così da poter rendere la nostra tavola ancora più speciale per tutti.<br><br>\
    La nostra casa è già arredata e piena d'amore. Tuttavia, se volete farci un dono gradito, preferiamo metterlo nel salvadanaio...<br>\
    iban: it93f0301503200000003641112"},
}

