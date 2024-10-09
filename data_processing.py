import pandas as pd
import streamlit as st


def load_file(file):
    try:
        if file.name.endswith('.csv'):
            return pd.read_csv(file)
        elif file.name.endswith(('.xlsx', '.xls')):
            return pd.read_excel(file, engine='openpyxl')
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
    return None


def compare_files(df1, df2):
    # Asegurarse de que ambos DataFrames tengan las mismas columnas
    common_columns = df1.columns.intersection(df2.columns)
    df1 = df1[common_columns]
    df2 = df2[common_columns]

    # Encontrar las filas que están en df1 pero no en df2
    diff1 = df1[~df1.apply(tuple, 1).isin(df2.apply(tuple, 1))]

    # Encontrar las filas que están en df2 pero no en df1
    diff2 = df2[~df2.apply(tuple, 1).isin(df1.apply(tuple, 1))]

    # Combinar las diferencias
    all_diff = pd.concat([diff1, diff2])

    # Agregar una columna para indicar la fuente de la diferencia
    all_diff['Fuente'] = ['Archivo 1'] * len(diff1) + ['Archivo 2'] * len(diff2)

    return all_diff