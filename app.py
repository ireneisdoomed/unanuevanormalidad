import streamlit as st
from PIL import Image
from src.query import query

header = Image.open("images/header.png")

st.image(header, width=800, format="PNG",  use_column_width=True)

st.header("¿Cuál es tu código postal?")
code = st.text_input("Inserta aquí tu código postal.")

if len(code) > 0:
    st.write("El código que has solicitado es", code, ".")
    result = query(code)
    if result == "1":
        info = open('src/fase0.md', 'r')
        st.markdown(info.read())

    elif result == "0":
        st.write("Ánimo! Tu fase", result)
    
