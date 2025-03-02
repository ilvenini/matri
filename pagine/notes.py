import streamlit as st
from modules import utils
import requests
    
def app():
    utils.set_font("Delius Swash Caps")
    #st.write("## Matrimonio di Annamaria e Andrea")
    
    user_id = utils.get_query_params()

    st.title("Conferma di partecipazione")

    st.write(USER_DATA['all']["text1"], unsafe_allow_html=True)

    TOKEN = st.secrets["BOT_TOKEN"] # BotFather
    CHAT_ID_ANDREA = st.secrets["CHAT_ID_ANDREA"]
    CHAT_ID_ANNA = st.secrets["CHAT_ID_ANNA"]    
    
    # Form Streamlit
    #st.title("Contattaci 📩")
    with st.form("form_contatto"):
        #nome = st.text_input("Nome", value=user_id)
        messaggio = st.text_area("Scrivici un messaggio!")
        submit = st.form_submit_button("Invia")
    
    if submit:
        #if nome and messaggio:
        if messaggio:
            utils.invia_telegram(user_id, messaggio)
            st.success("Messaggio inviato, grazie!")
        else:
            st.warning("Messaggio vuoto")

    st.divider()

    st.write(USER_DATA['all']["text2"], unsafe_allow_html=True)

# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "all": {"text1": "Per permetterci di organizzare al meglio la festa, vi chiediamo di **confermare la vostra presenza entro il 15 maggio**!<br><br>\
            Se avete **intolleranze, allergie alimentari o seguite una dieta vegetariana/vegana**, vi preghiamo di farcelo sapere.",
            "text2": "La nostra casa è già arredata e sufficientemente disordinata. Tuttavia, se volete farci un dono gradito, preferiamo metterlo nel salvadanaio.<br><br>\
            iban: it93f0301503200000003641112"},
}

