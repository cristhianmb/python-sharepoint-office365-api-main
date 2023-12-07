#Número de Contratos de Captación - 2021

import pandas as pd

def Indicador_14_2(df_hoja10_1, df_hoja2):
    df38 = df_hoja10_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
    df38['cve_periodo'] = df38['cve_periodo'] // 100
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado56 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df38[['dat_unidades', 'cve_periodo', 'cve_institucion']], how='left', left_on='claveinstitucion', right_on='cve_institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado56 = df_combinado56.groupby(['nombreinstitucion', 'claveinstitucion', 'cve_periodo', 'dat_unidades']).agg(
        Número_de_Contratos_de_Captación=('dat_unidades', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado56 = df_combinado56[df_combinado56['cve_periodo'] == 2021]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado56 = df_combinado56.groupby('nombreinstitucion').agg(
        Número_de_Contratos_de_Captación=('Número_de_Contratos_de_Captación', 'sum')
    ).reset_index()

    return df_combinado56
