# formato url: http://localhost:8501/?id=pietro

import streamlit as st
import os


# Pagine
#from pagine import home
#from pagine import location
#from pagine import notes

# Menu di navigazione
#PAGES = {
#    "🏠 Ciao!": home,
#    "🧭 Posizione": location,
#    "🎁 Conferma": notes
#}


#st.sidebar.title("Navigazione")
#selection = st.sidebar.selectbox("Seleziona una pagina:", list(PAGES.keys()))

#page = PAGES[selection]  # Esegue la pagina selezionata
#page.app()


st.set_page_config(page_title="App", page_icon="🌟", layout="wide")

# Dizionario per assegnare nomi leggibili ai file
pagine = {
    "🏠 Ciao!": "home.py",
    "🧭 Posizione": "location.py",
    "🎁 Conferma": "notes.py"
}


# Creare un menu personalizzato
pagina_scelta = st.sidebar.selectbox("📂 Navigazione", list(pagine.keys()))

# Eseguire il file corrispondente
file_pagina = f"pages/{pagine[pagina_scelta]}"
with open(file_pagina, "r", encoding="utf-8") as f:
    exec(f.read())

