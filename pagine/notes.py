import streamlit as st
from modules import utils
import requests
    
# Pagina 1: Personalizzata per ogni utente
def app():
    set_font("Delius Swash Caps")


# Funzione per ottenere il parametro "id" dall'URL
def get_query_params():
    query_params = st.query_params
    return query_params.get("id", None)

# Pagina 1: Personalizzata per ogni utente
def app():
    utils.set_font("Delius Swash Caps")
    #st.write("## Matrimonio di Annamaria e Andrea")
    
    user_id = get_query_params()
    if user_id and user_id in USER_DATA:
        st.write(USER_DATA[user_id]["text"], unsafe_allow_html=True)
    else:
        st.write(USER_DATA['all']["text"], unsafe_allow_html=True)

    TOKEN = st.secrets["BOT_TOKEN"] # BotFather
    CHAT_ID = st.secrets["CHAT_ID"]
    
    def invia_telegram(nome, messaggio):
        testo = f"📩 **Nuovo Messaggio!**\n👤 Nome: {nome}\n📝 Messaggio: {messaggio}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": testo, "parse_mode": "Markdown"})
    
    # Form Streamlit
    st.title("Contattaci! 📩")
    with st.form("form_contatto"):
        nome = st.code("Nome", value=user_id, language="markdown")
        messaggio = st.text_area("Messaggio")
        submit = st.form_submit_button("Invia")
    
    if submit:
        if nome and messaggio:
            invia_telegram(nome, messaggio)
            st.success("Messaggio inviato!")
        else:
            st.warning("Compila tutti i campi!")

    
# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "all": {"text": "Per permetterci di organizzare al meglio la festa, vi chiediamo di **confermare la vostra presenza entro il 15 maggio**!<br><br>\
    Se avete **intolleranze, allergie alimentari o seguite una dieta vegetariana/vegana**, vi preghiamo di farcelo sapere, così da poter rendere la nostra tavola ancora più speciale per tutti.<br><br>\
    La nostra casa è già arredata e piena d'amore. Tuttavia, se volete farci un dono gradito, preferiamo metterlo nel salvadanaio...<br>\
    iban: it93f0301503200000003641112"},
}

