#Monto del Gasto asociado - 2022 - Fraude externo

import pandas as pd

def Indicador_21_4(df_hoja12_0, df_hoja12_1, df_hoja12_2, df_hoja12_3, df_hoja2_1, df_hoja2):
    df92 = df_hoja12_0.copy()
    df93 = df_hoja12_1.copy()
    df94 = df_hoja12_2.copy()
    df95 = df_hoja12_3.copy()

    # Selecciona solo las columnas deseadas en cada DataFrame
    columnas_deseadas = ["Column1", "Column2", "Column10"]

    df92 = df_hoja12_0[columnas_deseadas]
    df93 = df_hoja12_1[columnas_deseadas]
    df94 = df_hoja12_2[columnas_deseadas]
    df95 = df_hoja12_3[columnas_deseadas]

    # Agrupa los DataFrames de manera vertical usando la función concat
    df_combinadoDel15 = pd.concat([df92, df93, df94, df95], ignore_index=True)

    # Filtrar por los valores deseados en 'Column10' (equivalente a 'Column11' en Excel)
    valores_filtrados3 = ['Fraude Externo', 'Fraude externo/Fraude con tarjetas bancarias']
    df_combinadoDel15_filtrado = df_combinadoDel15[df_combinadoDel15['Column10'].isin(valores_filtrados3)]

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado113_4 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df_combinadoDel15[['Column2', 'Column10']], how='left', left_on='claveinstitucion', right_on='Column2')

    df_combinado120 = df_combinado113_4.copy()
    df_combinado121 = df_combinado113_4.copy()

    df_combinado120 = df_combinado120[df_combinado120['Column10'] == 'Fraude Externo']
    df_combinado121 = df_combinado121[df_combinado121['Column10'] == 'Fraude externo/Fraude con tarjetas bancarias']

    # Agrupa y suma según tus necesidades
    df_combinado120 = df_combinado120.groupby(['nombreinstitucion']).agg(
        Monto_del_Gasto_asociado_Fraude_externo=('Column10', 'sum')
    ).reset_index()

    # Agrupa y suma según tus necesidades
    df_combinado121 = df_combinado121.groupby(['nombreinstitucion']).agg(
        Monto_del_Gasto_asociado_Fraude_externo=('Column10', 'sum')
    ).reset_index()

    df_combinado113_4 = pd.concat([df_combinado120, df_combinado121], ignore_index=True)

    # Realiza la agregación final sin repetir los valores de 'nombreinstitucion'
    df_combinado113_4 = df_combinado113_4.groupby('nombreinstitucion').agg(
        Monto_del_Gasto_asociado_Fraude_externo=('Monto_del_Gasto_asociado_Fraude_externo', 'count')
    ).reset_index()

    return df_combinado113_4

