import streamlit as st
from modules import utils

def app():
    utils.set_font("Crimson Text")
    #st.image("savethedate.png")
    #st.write("## Matrimonio di Annamaria e Andrea")
    user_id = utils.get_query_params()
    st.image("img/savethedate_alto.png")

    st.title("Dove celebreremo e dove festeggeremo")

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
    "all": {"text1": "La cerimonia si terrà alle ore **11.00** nel **Teatro Civico di Passirano**, di fronte alla piazza principale del paese, in via Garibaldi, 5.<br>",
            "text2": "A seguire, per il ricevimento, ci sposteremo nell'incantevole cantina **Bersi Serlini**, situata nel cuore della Franciacorta a **Provaglio d\'Iseo** (BS).",
            "text3": "I festeggiamenti inizieranno alle ore **12.30** e dureranno fino alle ore **20.30**.",
}
}