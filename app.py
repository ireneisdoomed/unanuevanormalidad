import streamlit as st
from PIL import Image
from src.query import query

header = Image.open("images/header.png")

st.image(header, width=800, format="PNG",  use_column_width=True)

st.header("¿Cuál es tu código postal?")
code = st.text_input("Inserta aquí tu código postal.")

if len(code) == 5:
    fase, territory = query(code)
    st.write(f"El código {code} corresponde a {territory}.")
    if fase == "1":
        info = open('data/fase1.md', 'r')
        st.markdown(info.read())

    elif fase == "0":
        info = open("data/fase0.md", "r")
        st.markdown(info.read())
    
elif len(code) != 0 and len(code) != 5:
    st.write("El código debe ser de 5 dígitos. Por favor, vuelve a intentarlo.")



st.markdown("""
        

        Wrote with 🧡 by [Irene López](https://github.com/ireneisdoomed).

        """)