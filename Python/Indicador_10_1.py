#Número de Contratos de crédito - Nómina - 2021
import pandas as pd

def Indicador_10_1(df_hoja3_1, df_hoja2):
    df10 = df_hoja3_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
    df10['cve_periodo'] = df10['cve_periodo'] // 100

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado28 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df10[['creditos', 'cve_institucion', 'cve_periodo']], how='left', left_on='claveinstitucion', right_on='cve_institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado28 = df_combinado28.groupby(['nombreinstitucion', 'cve_periodo']).agg(
        Número_de_Contratos_de_crédito_Nómina=('creditos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado28 = df_combinado28[df_combinado28['cve_periodo'] == 2022]
    
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['cve_periodo']
    df_combinado28=df_combinado28.drop(columna_eliminar,axis = 1)

    return df_combinado28
