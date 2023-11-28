#Número de Contratos de crédito - Personales - 2022
import pandas as pd

def Indicador_7_1(df_hoja7_1, df_hoja2):
    df7 = df_hoja7_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
    df7['cve_periodo'] = df7['cve_periodo'] // 100

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado25 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df7[['cve_periodo', 'cve_institucion', 'creditos']], how='left', left_on='claveinstitucion', right_on='cve_institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado25 = df_combinado25.groupby(['nombreinstitucion', 'cve_periodo', 'creditos']).agg(
        Número_de_Contratos_de_crédito_Personales=('creditos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado25 = df_combinado25[df_combinado25['cve_periodo'] == 2022]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado25 = df_combinado25.groupby('nombreinstitucion').agg(
        Número_de_Contratos_de_crédito_PersonalesD=('Número_de_Contratos_de_crédito_Personales', 'sum')
    ).reset_index()

    return df_combinado25
