# formato url: http://localhost:8501/?id=nome

import streamlit as st

# Pagine
from pagine import home
from pagine import location
from pagine import notes

st.set_page_config(
        page_title="Matrimonio di Annamaria e Andrea",
)

# Menu di navigazione
PAGES = {
    "🏠 Ciao!": home,
    #"🧭 Posizione": location,
    #"🎁 Conferma": notes
}


#st.sidebar.title("Navigazione")
selection = st.sidebar.selectbox("", list(PAGES.keys()))

page = PAGES[selection]  # Esegue la pagina selezionata
page.app()

