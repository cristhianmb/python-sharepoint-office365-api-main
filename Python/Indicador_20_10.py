#numero de operaciones a traves de Banca por Internet - 2021

import pandas as pd

def Indicador_20_10(df_hoja11_1, df_hoja2_1, df_hoja2):
    df80 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df80['Column1'] = df80['Column1'] // 100
    
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado110 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df80[['Column1', 'Column15','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado110 = df_combinado110.groupby(['nombreinstitucion', 'claveinstitucion', 'Column1', 'Column10']).agg(
        numero_de_operaciones_a_traves_de_Banca_por_Internet=('Column15', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado110 = df_combinado110[df_combinado110['Column1'] == 2021]
    df_combinado110 = df_combinado110[df_combinado110['Column10'] == 'Internet']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado110 = df_combinado110.groupby('nombreinstitucion').agg(
        numero_de_operaciones_a_traves_de_Banca_por_Internet=('numero_de_operaciones_a_traves_de_Banca_por_Internet', 'mean')
    ).reset_index()

    return df_combinado110
