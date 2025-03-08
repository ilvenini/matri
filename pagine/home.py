import streamlit as st
from modules import utils


# Pagina 1: Personalizzata per ogni utente
def app():
    utils.set_font("Delius Swash Caps")
    st.image("img/savethedate.png")
    st.title("Abbiamo provato a rimandarlo, ma...")

    
    user_id = utils.get_query_params()
    if user_id and user_id in USER_DATA:
        st.write(USER_DATA[user_id]["text"], unsafe_allow_html=True)
    else:
        st.warning("ID non valido o mancante. Contatta l'amministratore.")


# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "renny": {"text": ""},

    "michele": {"text": ""},

    "daniele": {"text": ""},

    "stefano": {"text": ""},

    "mauro": {"text": ""},

    "ziodaniele": {"text": ""},

    "ziorenato": {"text": ""},

    "ziavirgi": {"text": ""},

    "zioandrea": {"text": ""},

    "claudia": {"text": ""},

    "marco": {"text": ""},

    "michela": {"text": ""},

    "ziafranca": {"text": ""},

    "ziagio": {"text": ""},

    "chiara": {"text": ""},

    "silvia": {"text": ""},

    "ziagianna": {"text": ""},

    "manu": {"text": ""},

    "piera": {"text": ""},

    "vincenzo": {"text": ""},

    "rita": {"text": ""},

    "marcofederica": {"text": ""},

    "campa": {"text": ""},

    "zione": {"text": "Ciao **Zione bello!**<br><br>\
    Come sai, **domenica 15 giugno** sarà un giorno molto importante per me e Anna, e tu avrai un ruolo centrale, visto che avrai l'onore e l'onere di **celebrare** e **arringare**!<br><br>\
    Nel resto del sito abbiamo inserito le informazioni generiche riguardo location e orario del ricevimento, dove ci raggiungerà gran parte degli invitati.<br><br>\
    tuttavia, noi ti aspettiamo al **Comune di Passirano** per la cerimonia, che si svolgerà alle **ore 11.00**.<br><br>\
    Purtroppo, la sala può ospitare circa **20-25 persone**, per cui sarà una cosa molto intima.<br><br>\
    Dopodichè, alle ore **12.30** ci sposteremo nella Cantina Bersi Serlini a **Provaglio d\'Iseo**, dove ci sarà da mangiare, bere e festeggiare in abbondanza fino alle ore **21.00**.<br><br>\
    Non vediamo l'ora di goderci la bellissima giornata con te e famiglia!"},
    
    "snikuz": {"text": ""},

    "mura": {"text": ""},

    "flavietta": {"text": ""},

    "penela": {"text": ""},

    "pita": {"text": ""},

    "michelino": {"text": ""},

    "frenz": {"text": ""},

    "cischi": {"text": ""},

    "paletti": {"text": ""},

    "berto": {"text": ""},

    "stofen": {"text": ""},

    "naldo": {"text": ""},

    "ziotaffo": {"text": ""},

    "stesisti": {"text": ""},

    "danilo": {"text": ""},

    "flavio": {"text": ""},

    "paolo": {"text": ""},

    "diego": {"text": ""},

    "jessy": {"text": ""},

    "cri": {"text": ""},

    "andre": {"text": ""},

    "lucia": {"text": ""},

    "martina": {"text": ""},

    "ylenia": {"text": ""},

    "francesca": {"text": ""},

    "prova": {"text": "...**ci sposiamo**!<br> Cari Michele e Laura, l’appuntamento è per il **15 giugno 2025**.<br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br>\
    Dopo i sì” ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve! \
    Nelle prossime pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},
    
}
