import streamlit as st

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
