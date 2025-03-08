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



    st.divider()

    st.title("Dove celebreremo")

    st.write(USER_DATA['all']["text1"], unsafe_allow_html=True)

    st.image("img/teatro.png", width=1000)
    
    maps_url1 = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d12123.860374426948!2d10.058770042726522!3d45.59958349907525!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47816fef608b8eb5%3A0x77bdaf684b13c242!2sTeatro%20Civico!5e0!3m2!1sen!2sit!4v1741435496629!5m2!1sen!2sit"

    # Iframe responsive con larghezza dinamica
    st.markdown(
        f"""
        <iframe src="{maps_url1}" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        """,
        unsafe_allow_html=True
    )

    #st.image("img/bersi1.png")
    st.divider()

    st.title("Dove festeggeremo")

    st.write(USER_DATA['all']["text2"], unsafe_allow_html=True)

    st.write(USER_DATA['all']["text3"], unsafe_allow_html=True)

    st.image("img/bersi2.png")
    
    st.image("img/bersi3.png")

    maps_url2 = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d22317.578032493395!2d10.001761133153158!3d45.63681782190423!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x478165bef8329e71%3A0xe84fbfd81f60c13b!2sBersi%20Serlini%20Franciacorta!5e0!3m2!1sen!2sit!4v1740904038349!5m2!1sen!2sit"

    # Iframe responsive con larghezza dinamica
    st.markdown(
        f"""
        <iframe src="{maps_url2}" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.title("Conferma di partecipazione")

    st.write(USER_DATA['all']["text5"], unsafe_allow_html=True)
    
    # Form Streamlit
    #st.title("Contattaci 📩")
    with st.form("form_contatto"):
        #nome = st.text_input("Nome", value=user_id)
        messaggio = st.text_area("Scrivere qui per conferma")
        submit = st.form_submit_button("Invia")
    
    if submit:
        #if nome and messaggio:
        if messaggio:
            utils.invia_telegram(user_id, messaggio)
            st.success("Messaggio inviato, grazie!")
        else:
            st.warning("Messaggio vuoto")

    st.divider()

    st.write(USER_DATA['all']["text6"], unsafe_allow_html=True)



    st.image("img/savethedate_basso.png")


# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "renny": {"text": "...**ci sposiamo**!<br><br> Cari Renato e Margherita, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br>\
    Vi aspettiamo!"},
    
    "michele": {"text": "...**ci sposiamo**!<br><br> Cari Michele e Laura, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "daniele": {"text": "...**ci sposiamo**!<br><br> Ciao Daniele, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "stefano": {"text": "...**ci sposiamo**!<br><br> Cari Stefano, Jean e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "mauro": {"text": "...**ci sposiamo**!<br><br> Cari Mauro e Valeria, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "ziodaniele": {"text": "...**ci sposiamo**!<br><br> Cari zii Daniele e Ornella, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "ziorenato": {"text": "...**ci sposiamo**!<br><br> Cari zio Renato, zia Laura e Rossella, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "ziavirgi": {"text": "...**ci sposiamo**!<br><br> Cari zii Virgi e Gian, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "zioandrea": {"text": "...**ci sposiamo**!<br><br> Caro zio Andrea, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "claudia": {"text": "...**ci sposiamo**!<br><br> Cari Claudia, Max e ragazzi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "marco": {"text": "...**ci sposiamo**!<br><br> Cari Marco, Egle e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "michela": {"text": "...**ci sposiamo**!<br><br> Cari Michela ed Alessandro, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "ziafranca": {"text": "...**ci sposiamo**!<br><br> Cari zii Franca e Gabri, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "ziagio": {"text": "...**ci sposiamo**!<br><br> Cara Gio, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "chiara": {"text": "...**ci sposiamo**!<br><br> Cari Chiara, Marco e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "silvia": {"text": "...**ci sposiamo**!<br><br> Cari Silvia, Marco e ragazze, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "silvio": {"text": "...**ci sposiamo**!<br><br> Cari Silvio e Susanna, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "ziagianna": {"text": "...**ci sposiamo**!<br><br> Cari zii Gianna e Bruno, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "manu": {"text": "...**ci sposiamo**!<br><br> Cari Manu, Elisa e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "piera": {"text": "...**ci sposiamo**!<br><br> Cara mamma/nonna Piera, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "vincenzo": {"text": "...**ci sposiamo**!<br><br> Ciao bel Vincinsì, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "rita": {"text": "...**ci sposiamo**!<br><br> Cara zia e zia bis Rita, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "marcofederica": {"text": "...**ci sposiamo**!<br><br> Cari Marco, Federica e Irene, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "campa": {"text": "...**ci sposiamo**!<br><br> Cari Luca, Bea e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "zione": {"text": "...**ci sposiamo**!<br><br> Caro zione, Marsi e bimbi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},
    
    "snikuz": {"text": "...**ci sposiamo**!<br><br> Cara Zia Nico, Aga ed Ettore, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "mura": {"text": "...**ci sposiamo**!<br><br> Ciao Mura, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "flavietta": {"text": "...**ci sposiamo**!<br><br> Care Flavietta e Luna, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "penela": {"text": "...**ci sposiamo**!<br><br> Ciao Pennet, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "pita": {"text": "...**ci sposiamo**!<br><br> Ciao Pietro, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "michelino": {"text": "...**ci sposiamo**!<br><br> Ciao Michi, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "frenz": {"text": "...**ci sposiamo**!<br><br> Ciao Frenz, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "cischi": {"text": "...**ci sposiamo**!<br><br> Ciao Francesco, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "paletti": {"text": "...**ci sposiamo**!<br><br> Ciao Palettissimo, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "berto": {"text": "...**ci sposiamo**!<br><br> Cari Berto ed Angela, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "stofen": {"text": "...**ci sposiamo**!<br><br> Cari Stofen, Milena e Samuel, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "naldo": {"text": "...**ci sposiamo**!<br><br> Ciao Naldo, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "ziotaffo": {"text": "...**ci sposiamo**!<br><br> Ciao Zio Taffo, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "stesisti": {"text": "...**ci sposiamo**!<br><br> Cari Stefano e Laura, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "danilo": {"text": "...**ci sposiamo**!<br><br> Ciao Danilo, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "flavio": {"text": "...**ci sposiamo**!<br><br> Ciao Flavio, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "paolo": {"text": "...**ci sposiamo**!<br><br> Ciao Paolo, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "diego": {"text": "...**ci sposiamo**!<br><br> Ciao Diego, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "jessy": {"text": "...**ci sposiamo**!<br><br> Cari Jessica, Michael e Ruby, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "cry": {"text": "...**ci sposiamo**!<br><br> Cari Cristina ed Enrico, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "andre": {"text": "...**ci sposiamo**!<br><br> Ciao Andrea, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "lucy": {"text": "...**ci sposiamo**!<br><br> Ciao Lucia, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "marti": {"text": "...**ci sposiamo**!<br><br> Ciao Martina, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "ile": {"text": "...**ci sposiamo**!<br><br> Ciao Ilenia, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "fra": {"text": "...**ci sposiamo**!<br><br> Ciao Fra, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverai (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
\
    Ti aspettiamo!"},

    "standard": {"text": "...**ci sposiamo**!<br><br> Cari xxx, l’appuntamento è per il **15 giugno 2025**.<br><br>\
    Alle **11:00** ci troverete (emozionati e un po’ agitati) al **Teatro Civico di Passirano** per la cerimonia civile.<br><br>\
    Dopo i sì” ufficiali, ci sposteremo alla cantina **Bersi Serlini di Provaglio d'Iseo** per festeggiare come si deve!<br><br> \
    Vi aspettiamo!"},

    "all": {"text1": "La cerimonia si terrà alle ore **11.00** nel **Teatro Civico di Passirano**, di fronte alla piazza principale del paese, in via Garibaldi, 5.<br>",
            "text2": "A seguire, per il ricevimento, ci sposteremo nell'incantevole cantina **Bersi Serlini**, situata nel cuore della Franciacorta a **Provaglio d\'Iseo** (BS).",
            "text3": "I festeggiamenti inizieranno alle ore **12.30** e dureranno fino alle ore **20.30**.",
            "text5": "Per permetterci di organizzare al meglio la festa, si chiede di **confermare la presenza entro il 15 maggio**!<br><br>\
            In caso di **intolleranze, allergie alimentari o dieta vegetariana/vegana**, si prega di comunicarcelo.",
            "text6": "La nostra casa è già arredata e sufficientemente disordinata.<br>Tuttavia, per chi desidera farci un dono gradito, preferiamo metterlo nel salvadanaio.<br><br>\
            IBAN: IT93F0301503200000003641112 c/o Banca Fineco",},

    }
