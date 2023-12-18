#numero de operaciones en TPVs - 2021

import pandas as pd

def Indicador_20_8(df_hoja11_1, df_hoja2_1, df_hoja2):
    df77 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df77['Column1'] = df77['Column1'] // 100
    
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado108 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df77[['Column1', 'Column15','Column4', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado108 = df_combinado108.groupby(['nombreinstitucion', 'claveinstitucion', 'Column1', 'Column10']).agg(
        numero_de_operaciones_en_TPVs=('Column15', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado108 = df_combinado108[df_combinado108['Column1'] == 2021]
    df_combinado108 = df_combinado108[df_combinado108['Column10'] == 'TPV']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado108 = df_combinado108.groupby('nombreinstitucion').agg(
        numero_de_operaciones_en_TPVs=('numero_de_operaciones_en_TPVs', 'mean')
    ).reset_index()
    
    return df_combinado108
