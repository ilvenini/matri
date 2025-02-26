# formato url: http://localhost:8501/?id=pietro

import streamlit as st


# Pagine
from pages import home
from pages import location
from pages import notes

# Menu di navigazione
PAGES = {
    "🏠 Ciao!": home,
    "🧭 Posizione": location,
    "🎁 Conferma": notes
}


st.sidebar.title("Navigazione")
selection = st.sidebar.radio("Seleziona una pagina:", list(PAGES.keys()))



page = PAGES[selection]  # Esegue la pagina selezionata
page.app()
