import streamlit as st

def show_home():
    st.title("Conciliaciones")

    st.markdown("""
    Esta aplicación le permite comparar dos archivos y encontrar las diferencias entre ellos.

    ### Cómo usar la aplicación:

    1. Cargue dos archivos (Excel .xlsx o .xls) utilizando los botones de carga.
    2. Visualice los archivos cargados expandiendo las secciones correspondientes.
    3. Haga clic en "Comparar Archivos" para ver las diferencias.
    4. Descargue los resultados utilizando el botón "Descargar Resultados" (en formato Excel).

    Las diferencias mostradas son los elementos que están en un archivo pero no en el otro.
    """)