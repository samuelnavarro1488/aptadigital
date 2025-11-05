
st.set_page_config(page_title="Acta Digital", page_icon="📝")

st.title("📝 Acta Digital")
st.write("Aplicación básica de ejemplo creada con Streamlit.")

with st.form("form_acta"):
    titulo = st.text_input("Título del acta")
    asistentes = st.text_area("Asistentes (uno por línea)")
    acuerdos = st.text_area("Acuerdos tomados")
    fecha = st.date_input("Fecha del acta")
    enviar = st.form_submit_button("Generar acta")

if enviar:
    st.success("Acta generada correctamente:")
    st.write(f"**Título:** {titulo}")
    st.write(f"**Fecha:** {fecha}")
    st.write("**Asistentes:**")
    st.write(asistentes)
    st.write("**Acuerdos:**")
    st.write(acuerdos)

import streamlit as st
import hashlib, time, json

st.set_page_config(page_title="Imports Demo", page_icon="🧩")

st.title("🧩 Demo: streamlit + hashlib + time + json")

# --- hashlib: calcular hash SHA-256 de un texto ---
st.subheader("🔐 hashlib (SHA-256)")
texto = st.text_input("Escribe un texto para calcular su hash:")
if texto:
    sha256 = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    st.code(sha256, language="text")

# --- time: mostrar hora actual (en el momento del render) ---
st.subheader("⏱️ time (hora actual)")
st.write("Epoch (segundos):", int(time.time()))
st.write("Hora local:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# --- json: serializar un diccionario a JSON ---
st.subheader("🧾 json (serialización)")
datos = {
    "texto": texto,
    "hash_sha256": hashlib.sha256(texto.encode("utf-8")).hexdigest() if texto else None,
    "timestamp": int(time.time())
}
st.write("Diccionario Python:")
st.write(datos)

st.write("JSON (texto):")
st.code(json.dumps(datos, ensure_ascii=False, indent=2), language="json")

st.info("Tip: Recarga la página para actualizar la hora, o añade un st.button para refrescar.")
streamlit run app.py


