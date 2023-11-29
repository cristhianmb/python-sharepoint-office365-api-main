#Número de Contratos de crédito - Personales - 2021
import pandas as pd

def Indicador_10_4(df_hoja7_1, df_hoja2):
    df13 = df_hoja7_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
    df13['cve_periodo'] = df13['cve_periodo'] // 100

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado31 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df13[['creditos', 'cve_institucion', 'cve_periodo']], how='left', left_on='claveinstitucion', right_on='cve_institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado31 = df_combinado31.groupby(['nombreinstitucion', 'cve_periodo']).agg(
        Número_de_Contratos_de_crédito_Personales=('creditos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado31 = df_combinado31[df_combinado31['cve_periodo'] == 2022]

    # Eliminación de columnas sobrantes
    columna_eliminar = ['cve_periodo']
    df_combinado31 = df_combinado31.drop(columna_eliminar, axis=1)

    return df_combinado31
