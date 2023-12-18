#Monto del Gasto asociado - 2022 - Fraude externo

import pandas as pd

def Indicador_21_2(df_hoja12_0, df_hoja12_1, df_hoja12_2, df_hoja12_3, df_hoja2_1, df_hoja2):
    df87 = df_hoja12_0.copy()
    df88 = df_hoja12_1.copy()
    df89 = df_hoja12_2.copy()
    df90 = df_hoja12_3.copy()

    # Selecciona solo las columnas deseadas en cada DataFrame
    columnas_deseadas = ["Column1", "Column2", "Column3", "Column10", "Column13"]

    df87 = df_hoja12_0[columnas_deseadas]
    df88 = df_hoja12_1[columnas_deseadas]
    df89 = df_hoja12_2[columnas_deseadas]
    df90 = df_hoja12_3[columnas_deseadas]

    # Agrupa los DataFrames de manera vertical usando la función concat
    df_combinadoDel13 = pd.concat([df87, df88, df89, df90], ignore_index=True)

    # Filtrar por los valores deseados en 'Column10' (equivalente a 'Column11' en Excel)
    valores_filtrados1 = ['Fraude Externo', 'Fraude externo/Fraude con tarjetas bancarias']
    df_combinadoDel13_filtrado = df_combinadoDel13[df_combinadoDel13['Column10'].isin(valores_filtrados1)]

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado113_2 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df_combinadoDel13[['Column2', 'Column10','Column13']], how='left', left_on='claveinstitucion', right_on='Column2')

    df_combinado116 = df_combinado113_2.copy()
    df_combinado117 = df_combinado113_2.copy()

    df_combinado116 = df_combinado116[df_combinado116['Column10'] == 'Fraude Externo']
    df_combinado117 = df_combinado117[df_combinado117['Column10'] == 'Fraude externo/Fraude con tarjetas bancarias']

    # Agrupa y suma según tus necesidades
    df_combinado116 = df_combinado116.groupby(['nombreinstitucion']).agg(
        Monto_del_Gasto_asociado_Fraude_externo=('Column13', 'sum')
    ).reset_index()

    # Agrupa y suma según tus necesidades
    df_combinado117 = df_combinado117.groupby(['nombreinstitucion']).agg(
        Monto_del_Gasto_asociado_Fraude_externo=('Column13', 'sum')
    ).reset_index()

    df_combinado113_2 = pd.concat([df_combinado116, df_combinado116], ignore_index=True)

    # Realiza la agregación final sin repetir los valores de 'nombreinstitucion'
    df_combinado113_2 = df_combinado113_2.groupby('nombreinstitucion').agg(
        Monto_del_Gasto_asociado_Fraude_externo=('Monto_del_Gasto_asociado_Fraude_externo', 'sum')
    ).reset_index()
    
    return df_combinado113_2



