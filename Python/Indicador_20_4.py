#número de operaciones en ATMs - 2021

import pandas as pd

def Indicador_20_4(df_hoja11_1, df_hoja2_1, df_hoja2):

    df73 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df73['Column1'] = df73['Column1'] // 100
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado105 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df73[['Column1', 'Column15','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado105 = df_combinado105.groupby(['nombreinstitucion', 'claveinstitucion', 'Column1', 'Column10']).agg(
        numero_de_operaciones_en_ATMs=('Column15', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado105 = df_combinado105[df_combinado105['Column1'] == 2021]
    df_combinado105 = df_combinado105[df_combinado105['Column10'] == 'Cajero Automático']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado105 = df_combinado105.groupby('nombreinstitucion').agg(
        numero_de_operaciones_en_ATMs=('numero_de_operaciones_en_ATMs', 'mean')
    ).reset_index()

    return df_combinado105
