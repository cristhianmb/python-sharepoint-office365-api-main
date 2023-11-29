#Número de Contratos de crédito - Automotriz - 2021
import pandas as pd

def Indicador_10_2(df_hoja5_1, df_hoja2):
    
    df11 = df_hoja5_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
    df11['cve_periodo'] = df11['cve_periodo'] // 100

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado29 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df11[['creditos', 'cve_institucion', 'cve_periodo']], how='left', left_on='claveinstitucion', right_on='cve_institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado29 = df_combinado29.groupby(['nombreinstitucion', 'cve_periodo']).agg(
        Número_de_Contratos_de_crédito_Automotriz=('creditos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado29 = df_combinado29[df_combinado29['cve_periodo'] == 2022]
    
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['cve_periodo']
    df_combinado29=df_combinado29.drop(columna_eliminar,axis = 1)

    return df_combinado29
