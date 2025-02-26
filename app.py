# formato url: http://localhost:8501/?id=pietro

import streamlit as st


# Pagine
from pagine import home
from pagine import location
from pagine import notes

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
