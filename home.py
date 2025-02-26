import streamlit as st
from utils import set_font


# Funzione per ottenere il parametro "id" dall'URL
def get_query_params():
    query_params = st.query_params
    return query_params.get("id", None)

# Pagina 1: Personalizzata per ogni utente
def app():
    set_font("Delius Swash Caps")
    st.image("savethedate.png")
    #st.write("## Matrimonio di Annamaria e Andrea")

    
    user_id = get_query_params()
    if user_id and user_id in USER_DATA:
        st.write(USER_DATA[user_id]["text"], unsafe_allow_html=True)
    else:
        st.warning("ID non valido o mancante. Contatta l'amministratore.")


# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "pietro": {"text": "Ciao **Zione bello!**<br><br>\
    Come sai, **domenica 15 giugno** sarà un giorno molto importante per me e Anna, e tu avrai un ruolo centrale, visto che avrai l'onore e l'onere di **celebrare** e **arringare**!<br><br>\
    Nel resto del sito abbiamo inserito le informazioni generiche riguardo location e orario del ricevimento, dove ci raggiungerà gran parte degli invitati.<br><br>\
    tuttavia, noi ti aspettiamo al **Comune di Passirano** per la cerimonia, che si svolgerà alle **ore 11.00**.<br><br>\
    Purtroppo, la sala può ospitare circa **20-25 persone**, per cui sarà una cosa molto intima.<br><br>\
    Dopodichè, alle ore **12.30** ci sposteremo nella Cantina Bersi Serlini a **Provaglio d\'Iseo**, dove ci sarà da mangiare, bere e festeggiare in abbondanza fino alle ore **21.00**.<br><br>\
    Non vediamo l'ora di goderci la bellissima giornata con te e famiglia!"},
    
    "michele": {"text": "Cari Michele e Laura,<br>\
Siamo felicissimi di invitarvi al nostro matrimonio! 💍✨\
Ci sposeremo il 15 giugno 2025 e non vediamo l’ora di festeggiare con voi.<br>\
Il rito civile sarà celebrato alle 11:00 presso il Comune di Passirano.<br>\
Dopo la cerimonia, ci sposteremo alla cantina Bersi Serlini di Provaglio d'Iseo, dove brinderemo e festeggeremo insieme questa giornata speciale.<br>\
Speriamo di avervi con noi! ❤️"},
    
    "user3": {"text": "Ciao Luca! Ecco il tuo contenuto."}
}
