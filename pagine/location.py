import streamlit as st
from modules import utils

def app():
    utils.set_font("Delius Swash Caps")
    #st.image("savethedate.png")
    #st.write("## Matrimonio di Annamaria e Andrea")
    user_id = utils.get_query_params()

    st.title("Dove celebreremo e dove festeggeremo")

    st.write(USER_DATA['all']["text1"], unsafe_allow_html=True)

    st.image("img/comune.jpg", width=1000)

    maps_url1 = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2791.6066051683956!2d10.062547311053198!3d45.59845250148086!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47816fef53b5a2a9%3A0x23d07dd3c0e21666!2sPiazza%20Europa%2C%2016%2C%2025050%20Passirano%20BS!5e0!3m2!1sen!2sit!4v1740904151382!5m2!1sen!2sit"

    # Iframe responsive con larghezza dinamica
    st.markdown(
        f"""
        <iframe src="{maps_url1}" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        """,
        unsafe_allow_html=True
    )

    #st.image("img/bersi1.png")
    st.divider()

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

# Dizionario con messaggi e immagini personalizzate
USER_DATA = {
    "all": {"text1": "La cerimonia si terrà nella sala civica del **Comune di Passirano** alle ore **11.30**.<br>",
            "text2": "A seguire, per il ricevimento, ci sposteremo nell'incantevole cantina **Bersi Serlini**, situata nel cuore della Franciacorta a **Provaglio d\'Iseo** (BS).",
           "text3": "I festeggiamenti inizieranno alle ore **12.30** e dureranno fino alle ore **20.30**.",
}
}