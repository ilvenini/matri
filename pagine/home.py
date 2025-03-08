import streamlit as st
from modules import utils


# Pagina 1: Personalizzata per ogni utente
def app():
    utils.set_font("Crimson Text")
    st.image("img/savethedate_home.png")
    st.title("Abbiamo provato a rimandarlo, ma...")

    
    user_id = utils.get_query_params()
    if user_id and user_id in USER_DATA:
        st.write(USER_DATA[user_id]["text"], unsafe_allow_html=True)
    else:
        st.write("", unsafe_allow_html=True)
        #st.warning("")

    st.image("img/savethedate_basso.png")


# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "renny": {"text": "...**ci sposiamo**!<br><br> Cari Renato e Margherita, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},
    
    "michele": {"text": "...**ci sposiamo**!<br><br> Cari Michele e Laura, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "daniele": {"text": "...**ci sposiamo**!<br><br> Ciao Daniele, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "stefano": {"text": "...**ci sposiamo**!<br><br> Cari Stefano, Jean e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "mauro": {"text": "...**ci sposiamo**!<br><br> Cari Mauro e Valeria, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "ziodaniele": {"text": "...**ci sposiamo**!<br><br> Cari zii Daniele e Ornella, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "ziorenato": {"text": "...**ci sposiamo**!<br><br> Cari zio Renato, zia Laura e Rossella, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "ziavirgi": {"text": "...**ci sposiamo**!<br><br> Cari zii Virgi e Gian, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "zioandrea": {"text": "...**ci sposiamo**!<br><br> Caro zio Andrea, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "claudia": {"text": "...**ci sposiamo**!<br><br> Cari Claudia, Max e ragazzi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "marco": {"text": "...**ci sposiamo**!<br><br> Cari Marco, Egle e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "michela": {"text": "...**ci sposiamo**!<br><br> Cari Michela ed Alessandro, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "ziafranca": {"text": "...**ci sposiamo**!<br><br> Cari zii Franca e Gabri, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "ziagio": {"text": "...**ci sposiamo**!<br><br> Cara Gio, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "chiara": {"text": "...**ci sposiamo**!<br><br> Cari Chiara, Marco e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "silvia": {"text": "...**ci sposiamo**!<br><br> Cari Silvia, Marco e ragazze, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "silvio": {"text": "...**ci sposiamo**!<br><br> Cari Silvio e Susanna, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "ziagianna": {"text": "...**ci sposiamo**!<br><br> Cari zii Gianna e Bruno, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "manu": {"text": "...**ci sposiamo**!<br><br> Cari Manu, Elisa e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "piera": {"text": "...**ci sposiamo**!<br><br> Cara mamma/nonna Piera, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "vincenzo": {"text": "...**ci sposiamo**!<br><br> Ciao bel Vincinsì, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "rita": {"text": "...**ci sposiamo**!<br><br> Cara zia e zia bis Rita, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "marcofederica": {"text": "...**ci sposiamo**!<br><br> Cari Marco, Federica e Irene, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "campa": {"text": "...**ci sposiamo**!<br><br> Cari Luca, Bea e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "zione": {"text": "...**ci sposiamo**!<br><br> Caro zione, Marsi e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},
    
    "snikuz": {"text": "...**ci sposiamo**!<br><br> Cara Zia Nico, Aga ed Ettore, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "mura": {"text": "...**ci sposiamo**!<br><br> Ciao Mura, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "flavietta": {"text": "...**ci sposiamo**!<br><br> Care Flavietta e Luna, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "penela": {"text": "...**ci sposiamo**!<br><br> Ciao Pennet, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "pita": {"text": "...**ci sposiamo**!<br><br> Ciao Pietro, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "michelino": {"text": "...**ci sposiamo**!<br><br> Ciao Michi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "frenz": {"text": "...**ci sposiamo**!<br><br> Ciao Frenz, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "cischi": {"text": "...**ci sposiamo**!<br><br> Ciao Francesco, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "paletti": {"text": "...**ci sposiamo**!<br><br> Ciao Palettissimo, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "berto": {"text": "...**ci sposiamo**!<br><br> Cari Berto ed Angela, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "stofen": {"text": "...**ci sposiamo**!<br><br> Cari Stofen, Milena e Samuel, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "naldo": {"text": "...**ci sposiamo**!<br><br> Ciao Naldo, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "ziotaffo": {"text": "...**ci sposiamo**!<br><br> Ciao Zio Taffo, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "stesisti": {"text": "...**ci sposiamo**!<br><br> Cari Stefano e Laura, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "danilo": {"text": "...**ci sposiamo**!<br><br> Ciao Danilo, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "flavio": {"text": "...**ci sposiamo**!<br><br> Ciao Flavio, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "paolo": {"text": "...**ci sposiamo**!<br><br> Ciao Paolo, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "diego": {"text": "...**ci sposiamo**!<br><br> Ciao Diego, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "jessy": {"text": "...**ci sposiamo**!<br><br> Cari Jessica, Michael e Ruby, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "cry": {"text": "...**ci sposiamo**!<br><br> Cari Cristina ed Enrico, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

    "andre": {"text": "...**ci sposiamo**!<br><br> Ciao Andrea, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "lucy": {"text": "...**ci sposiamo**!<br><br> Ciao Lucia, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "marti": {"text": "...**ci sposiamo**!<br><br> Ciao Martina, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "ile": {"text": "...**ci sposiamo**!<br><br> Ciao Ilenia, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "fra": {"text": "...**ci sposiamo**!<br><br> Ciao Fra, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovi qualche dettaglio in più.<br><br>\
    Ti aspettiamo!"},

    "standard": {"text": "...**ci sposiamo**!<br><br> Cari xxx, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì” ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Nelle altre pagine trovate qualche dettaglio in più.<br><br>\
    Vi aspettiamo!"},

}
