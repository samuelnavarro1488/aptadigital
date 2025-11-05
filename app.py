# app.py
import streamlit as st
import hashlib, time, json

st.set_page_config(page_title="Demo Hash + JSON", page_icon="🔐")

st.title("Demo: hashlib + time + json en Streamlit (sin instalar nada local)")
st.write("Esta app se ejecuta en la nube. Usa solo librerías estándar y Streamlit.")

texto = st.text_input("Texto a hashear", "hola mundo")
algoritmo = st.selectbox("Algoritmo", ["md5", "sha1", "sha256", "sha512"])
espera = st.slider("Espera (segundos) con time.sleep()", 0, 3, 0)

if st.button("Calcular"):
    # Simular trabajo
    if espera:
        time.sleep(espera)

    # Elegir hash
    data = texto.encode("utf-8")
    h = getattr(hashlib, algoritmo)(data).hexdigest()

    resultado = {
        "input": texto,
        "algoritmo": algoritmo,
        "hash": h,
        "timestamp": int(time.time()),
    }

    st.success("Listo")
    st.write("**Hash:**", h)
    st.write("**Timestamp:**", resultado["timestamp"])
    st.subheader("JSON")
    st.code(json.dumps(resultado, ensure_ascii=False, indent=2), language="json")
streamlit

