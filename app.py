import streamlit as st
import pandas as pd
import io
from home import show_home
from data_processing import load_file, compare_files


def main():
    st.set_page_config(page_title="Conciliaciones Simples", layout="wide")

    show_home()

    st.header("Cargar Archivos")
    col1, col2 = st.columns(2)

    with col1:
        file1 = st.file_uploader("Cargue el archivo 1", type=["csv", "xlsx", "xls"])
        if file1:
            df1 = load_file(file1)
            with st.expander("Ver archivo 1"):
                st.dataframe(df1)
            st.session_state['df1'] = df1

    with col2:
        file2 = st.file_uploader("Cargue el archivo 2", type=["csv", "xlsx", "xls"])
        if file2:
            df2 = load_file(file2)
            with st.expander("Ver archivo 2"):
                st.dataframe(df2)
            st.session_state['df2'] = df2

    if 'df1' in st.session_state and 'df2' in st.session_state:
        if st.button("Comparar Archivos"):
            differences = compare_files(st.session_state['df1'], st.session_state['df2'])
            st.header("Resultados de la Comparación")
            st.dataframe(differences)

            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                differences.to_excel(writer, sheet_name='Diferencias', index=False)
            output.seek(0)

            st.download_button(
                label="Descargar Resultados",
                data=output,
                file_name="diferencias.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )


if __name__ == "__main__":
    main()