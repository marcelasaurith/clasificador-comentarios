#%%writefile app.py
import streamlit as st
from pymongo import MongoClient
import datetime

# Conexión a MongoDB Atlas
client = MongoClient("mongodb+srv://edithsaurith:CtrlMarce_2024@cluster0.ag2ioyk.mongodb.net/?retryWrites=true&w=majority")
db = client["equipo_3"]
collection = db["comentarios"]

# Clasificador simple (puedes reemplazarlo por tu modelo si deseas)
def clasificar_comentario(texto):
    texto = texto.lower()
    if any(palabra in texto for palabra in ["malo", "terrible", "horrible", "pésimo", "deficiente"]):
        return "Negativo"
    elif any(palabra in texto for palabra in ["bueno", "excelente", "maravilloso", "increíble", "recomendado"]):
        return "Positivo"
    else:
        return "Neutro"

# Interfaz
st.title("📋 Clasificador y Registro de Comentarios")

cliente_id = st.text_input("🆔 ID del Cliente")
canal = st.selectbox("🌐 Canal", ["Web", "WhatsApp", "Tienda física", "Llamada", "Otro"])
categoria = st.selectbox("📦 Categoría del producto", ["Electrónica", "Ropa", "Alimentos", "Hogar", "Otros"])
comentario = st.text_area("📝 Escribe tu comentario")

if st.button("📤 Enviar comentario"):
    if comentario.strip() and cliente_id.strip():
        clasificacion = clasificar_comentario(comentario)
        documento = {
            "cliente_id": cliente_id,
            "canal": canal,
            "categoria": categoria,
            "comentario": comentario,
            "clasificacion": clasificacion,
            "fecha": datetime.datetime.now()
        }
        collection.insert_one(documento)
        st.success(f"✅ Documento guardado correctamente. Clasificación: **{clasificacion}**")
    else:
        st.warning("⚠️ Por favor completa todos los campos obligatorios.")
