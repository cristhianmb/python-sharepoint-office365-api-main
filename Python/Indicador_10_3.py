#Número de Contratos de crédito - Automotriz - 2021
import pandas as pd

def Indicador_10_3(df_hoja6_1, df_hoja2):
    df12 = df_hoja6_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
    df12['cve_periodo'] = df12['cve_periodo'] // 100

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado30 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df12[['creditos', 'cve_institucion', 'cve_periodo']], how='left', left_on='claveinstitucion', right_on='cve_institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado30 = df_combinado30.groupby(['nombreinstitucion', 'cve_periodo']).agg(
        Número_de_Contratos_de_crédito_Automotriz=('creditos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado30 = df_combinado30[df_combinado30['cve_periodo'] == 2022]
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['cve_periodo']
    df_combinado30 = df_combinado30.drop(columna_eliminar, axis=1)

    return df_combinado30
