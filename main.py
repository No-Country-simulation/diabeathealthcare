import streamlit as st
from nutritional_info.services.get_nutritional_info import get_nutritional_info
from app.main import app_logic

st.set_page_config(
    page_title="Sistema de Recomendación de Dietas para Diabéticos",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.header("️🍏 Secciones")
options = ["Información Nutricional", "Recomendaciones de Dieta", "Estadísticas"]
selection = st.sidebar.radio("Seleccionar Opción", options)

st.title("️🍏 Sistema de Recomendación Nutricional para Personas con Diabetes")

if selection == "Información Nutricional":
    st.subheader("Información Nutricional")
    search_type = st.selectbox("Seleccione el tipo de búsqueda",
                               ["Código de barras", "Nombre del producto", "Imagen del producto"])

    if search_type in ["Código de barras", "Nombre del producto"]:
        input_text = st.text_input(f"Ingrese el {search_type.lower()}")
        image_upload = None
    else:
        input_text = None

    if search_type == "Imagen del producto":
        image_upload = st.file_uploader("Sube una imagen del producto", type=["jpg", "png"])

    if st.button("Obtener Información Nutricional"):
        response = get_nutritional_info(input_text, image_upload, search_type)
        if response:
            st.write(response)

elif selection == "Recomendaciones de Dieta":
    st.subheader("Recomendaciones de Dieta")
    app_logic()



elif selection == "Estadísticas":
    st.subheader("Estadísticas")