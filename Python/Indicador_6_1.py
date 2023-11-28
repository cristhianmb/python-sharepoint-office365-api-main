#Número de Contratos de crédito - ABCD - 2022
import pandas as pd

def Indicador_6_1(df_hoja6_1, df_hoja2):
    df6 = df_hoja6_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
    df6['cve_periodo'] = df6['cve_periodo'] // 100

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado24 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df6[['cve_periodo', 'cve_institucion', 'creditos']], how='left', left_on='claveinstitucion', right_on='cve_institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado24 = df_combinado24.groupby(['nombreinstitucion', 'cve_periodo', 'creditos']).agg(
        Número_de_Contratos_de_crédito_ABCD=('creditos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado24 = df_combinado24[df_combinado24['cve_periodo'] == 2022]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado24 = df_combinado24.groupby('nombreinstitucion').agg(
        Número_de_Contratos_de_crédito_ABCD=('Número_de_Contratos_de_crédito_ABCD', 'sum')
    ).reset_index()

    return df_combinado24
