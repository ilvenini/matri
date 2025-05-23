import streamlit as st
from modules import utils
    
def app():
    utils.set_font("Crimson Text")
    #st.write("## Matrimonio di Annamaria e Andrea")
    
    user_id = utils.get_query_params()

    st.image("img/savethedate_alto.png")

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


# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "all": {"text5": "Per permetterci di organizzare al meglio la festa, si chiede di **confermare la presenza entro il 15 maggio**!<br><br>\
            In caso di **intolleranze, allergie alimentari o dieta vegetariana/vegana**, si prega di comunicarcelo.",
            "text6": "La nostra casa è già arredata e sufficientemente disordinata.<br>Tuttavia, per chi desidera farci un dono gradito, preferiamo metterlo nel salvadanaio.<br><br>\
            IBAN: IT93F0301503200000003641112 c/o Banca Fineco"},
}

