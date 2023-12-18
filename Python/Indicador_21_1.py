#Monto de la perdida - 2022 - Fraude externo

import pandas as pd

def Indicador_21_1(df_hoja12_0, df_hoja12_1, df_hoja12_2, df_hoja12_3, df_hoja2_1, df_hoja2):
    df83 = df_hoja12_0.copy()
    df84 = df_hoja12_1.copy()
    df85 = df_hoja12_2.copy()
    df86 = df_hoja12_3.copy()

    # Selecciona solo las columnas deseadas en cada DataFrame
    columnas_deseadas = ["Column1", "Column2", "Column3", "Column10", "Column12"]

    df83 = df_hoja12_0[columnas_deseadas]
    df84 = df_hoja12_1[columnas_deseadas]
    df85 = df_hoja12_2[columnas_deseadas]
    df86 = df_hoja12_3[columnas_deseadas]

    # Agrupa los DataFrames de manera vertical usando la función concat
    df_combinadoDel12 = pd.concat([df83, df84, df85, df86], ignore_index=True)

    # Filtrar por los valores deseados en 'Column10' (equivalente a 'Column11' en Excel)
    valores_filtrados = ['Fraude Externo', 'Fraude externo/Fraude con tarjetas bancarias']
    df_combinadoDel12_filtrado = df_combinadoDel12[df_combinadoDel12['Column10'].isin(valores_filtrados)]

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado113 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df_combinadoDel12[['Column2', 'Column10','Column12']], how='left', left_on='claveinstitucion', right_on='Column2')

    df_combinado114 = df_combinado113.copy()
    df_combinado115 = df_combinado113.copy()

    df_combinado114 = df_combinado114[df_combinado114['Column10'] == 'Fraude Externo']
    df_combinado115 = df_combinado115[df_combinado115['Column10'] == 'Fraude externo/Fraude con tarjetas bancarias']

    # Agrupa y suma según tus necesidades
    df_combinado114 = df_combinado114.groupby(['nombreinstitucion']).agg(
        Monto_de_la_perdida_Fraude_externo=('Column12', 'sum')
    ).reset_index()

    # Agrupa y suma según tus necesidades
    df_combinado115 = df_combinado115.groupby(['nombreinstitucion']).agg(
        Monto_de_la_perdida_Fraude_externo=('Column12', 'sum')
    ).reset_index()

    df_combinado113 = pd.concat([df_combinado114, df_combinado115], ignore_index=True)

    # Realiza la agregación final sin repetir los valores de 'nombreinstitucion'
    df_combinado113 = df_combinado113.groupby('nombreinstitucion').agg(
        Monto_de_la_perdida_Fraude_externo=('Monto_de_la_perdida_Fraude_externo', 'sum')
    ).reset_index()

    return df_combinado113
