import streamlit as st
from modules import utils
import requests
    
def app():
    utils.set_font("Delius Swash Caps")
    #st.write("## Matrimonio di Annamaria e Andrea")
    
    user_id = utils.get_query_params()
    if user_id and user_id in USER_DATA:
        st.write(USER_DATA[user_id]["text"], unsafe_allow_html=True)
    else:
        st.write(USER_DATA['all']["text"], unsafe_allow_html=True)

    TOKEN = st.secrets["BOT_TOKEN"] # BotFather
    CHAT_ID_ANDREA = st.secrets["CHAT_ID_ANDREA"]
    CHAT_ID_ANNA = st.secrets["CHAT_ID_ANNA"]
    
    
    def invia_telegram(nome, messaggio):
        testo = f"📩 **Nuovo Messaggio!**\n👤 Nome: {nome}\n📝 Messaggio: {messaggio}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": testo, "parse_mode": "Markdown"})
    
    # Form Streamlit
    #st.title("Contattaci 📩")
    with st.form("form_contatto"):
        #nome = st.text_input("Nome", value=user_id)
        messaggio = st.text_area("Scrivici un messaggio!")
        submit = st.form_submit_button("Invia")
    
    if submit:
        #if nome and messaggio:
        if messaggio:
            invia_telegram(user_id, messaggio)
            st.success("Messaggio inviato, grazie!")
        else:
            st.warning("Messaggio vuoto")

    
# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "all": {"text": "Per permetterci di organizzare al meglio la festa, vi chiediamo di **confermare la vostra presenza entro il 15 maggio**!<br><br>\
    Se avete **intolleranze, allergie alimentari o seguite una dieta vegetariana/vegana**, vi preghiamo di farcelo sapere, così da poter rendere la nostra tavola ancora più speciale per tutti.<br><br>\
    La nostra casa è già arredata e piena d'amore. Tuttavia, se volete farci un dono gradito, preferiamo metterlo nel salvadanaio...<br>\
    iban: it93f0301503200000003641112"},
}

