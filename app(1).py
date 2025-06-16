import streamlit as st
from pymongo import MongoClient
import datetime

# Conexión a MongoDB Atlas
client = MongoClient("mongodb+srv://edithsaurith:CtrlMarce_2024@cluster0.ag2ioyk.mongodb.net/?retryWrites=true&w=majority")  # <-- Reemplaza esto por tu URI real
db = client["equipo_3"]
collection = db["comentarios"]

# Clasificador simple de ejemplo
def clasificar_comentario(texto):
    texto = texto.lower()
    if "malo" in texto or "terrible" in texto or "horrible" in texto:
        return "Negativo"
    elif "excelente" in texto or "bueno" in texto or "maravilloso" in texto:
        return "Positivo"
    else:
        return "Neutro"

# Interfaz de usuario
st.title("Clasificador de Comentarios")

comentario = st.text_area("Escribe tu comentario aquí:")

if st.button("Enviar comentario"):
    if comentario.strip() != "":
        clasificacion = clasificar_comentario(comentario)
        documento = {
            "comentario": comentario,
            "clasificacion": clasificacion,
            "fecha": datetime.datetime.now()
        }
        collection.insert_one(documento)
        st.success(f"✅ Comentario clasificado como: **{clasificacion}** y guardado en MongoDB.")
    else:
        st.warning("⚠️ Escribe un comentario antes de enviarlo.")
