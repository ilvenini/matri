import streamlit as st
from modules import utils


# Funzione per ottenere il parametro "id" dall'URL
def get_query_params():
    query_params = st.query_params
    return query_params.get("id", None)

# Pagina 1: Personalizzata per ogni utente
def app():
    utils.set_font("Delius Swash Caps")
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
    
    "annamaria": {"text": "Dopo il 'sì', vogliamo festeggiare insieme a voi con una giornata speciale all’insegna del buon cibo, dell’ottimo vino e della compagnia migliore!<br><br>\
    Vi aspettiamo alle **12:30** per dare inizio ai festeggiamenti, che proseguiranno fino alle ore **21:00**, in una splendida cantina nel cuore della Franciacorta.<br><br>\
    Brinderemo con calici di vino pregiato, immersi in un’atmosfera incantevole, tra risate, brindisi e momenti indimenticabili.<br><br>\
    Non vediamo l’ora di condividere questa giornata con voi!"},
    
    "michele": {"text": "Cari Michele e Laura,<br>\
    Siamo felici di invitarvi al nostro matrimonio!<br><br>\
    Ci sposeremo il **15 giugno 2025** e non vediamo l’ora di festeggiare.<br><br>\
    Il rito civile sarà celebrato alle **11:00** presso il Comune di Passirano.<br>\
    Dopo la cerimonia, ci sposteremo alla cantina Bersi Serlini di Provaglio d'Iseo, dove brinderemo e festeggeremo insieme questa giornata speciale.<br>\
    Speriamo di avervi con noi! ❤️"},
}
