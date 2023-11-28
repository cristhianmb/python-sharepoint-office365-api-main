#Número de Contratos de crédito - Automotriz - 2022
import pandas as pd

def Indicador_5_1(df_hoja5_1, df_hoja2):
    df5 = df_hoja5_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
    df5['cve_periodo'] = df5['cve_periodo'] // 100

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado23 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df5[['cve_periodo', 'cve_institucion', 'creditos']], how='left', left_on='claveinstitucion', right_on='cve_institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado23 = df_combinado23.groupby(['nombreinstitucion', 'cve_periodo', 'creditos']).agg(
        Número_de_Contratos_de_crédito_Automotriz=('creditos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado23 = df_combinado23[df_combinado23['cve_periodo'] == 2022]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado23 = df_combinado23.groupby('nombreinstitucion').agg(
        Número_de_Contratos_de_crédito_Automotriz=('Número_de_Contratos_de_crédito_Automotriz', 'sum')
    ).reset_index()

    return df_combinado23
