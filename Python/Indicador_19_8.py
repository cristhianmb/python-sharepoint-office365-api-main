#número de Corresponsales - 2022

import pandas as pd

def Indicador_19_8(df_hoja11_1, df_hoja2_1, df_hoja2):
    # Codigo de prueba con calculos ya utilizados en el programa
    df68 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df68['Column1'] = df68['Column1'] // 100
    
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado100 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']],
                               df68[['Column1','Column4', 'Column10']],
                               how='left',
                               left_on='claveinstitucion',
                               right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado100 = df_combinado100.groupby(['nombreinstitucion', 'claveinstitucion', 'Column10', 'Column1']).agg(
        numero_de_Corresponsales=('Column10', 'count')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado100 = df_combinado100[df_combinado100['Column1'] == 2021]
    df_combinado100 = df_combinado100[df_combinado100['Column10'] == 'Comisionistas']

    # Eliminación de columnas sobrantes
    columna_eliminar = ['Column10', 'claveinstitucion', 'Column1']
    df_combinado100 = df_combinado100.drop(columna_eliminar, axis=1)

    return df_combinado100
