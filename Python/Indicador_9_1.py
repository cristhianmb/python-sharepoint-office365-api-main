#Número de Contratos de crédito - Vivienda -2021
import pandas as pd

def Indicador_9_1(df_hoja3_1, df_hoja2):
    # Copiar el DataFrame df_hoja3_1 para trabajar con él
    df9 = df_hoja3_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
    df9['cve_periodo'] = df9['cve_periodo'] // 100

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado27 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df9[['dat_id_credito_met_cnbv', 'cve_moneda', 'cve_periodo', 'cve_institucion']], how='left', left_on='claveinstitucion', right_on='cve_institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado27 = df_combinado27.groupby(['nombreinstitucion', 'cve_periodo', 'dat_id_credito_met_cnbv', 'cve_moneda']).agg(
        Número_de_Contratos_de_crédito_Vivienda=('cve_periodo', 'sum')
    ).reset_index()

    # Filtrar por la moneda deseada (99)
    df_combinado27 = df_combinado27[df_combinado27['cve_moneda'] == 99]

    # Filtrar por el periodo deseado (2022)
    df_combinado27 = df_combinado27[df_combinado27['cve_periodo'] == 2022]

    # Agrupar nuevamente para tomar el primer valor no nulo de 'nombreinstitucion' por grupo
    df_combinado27 = df_combinado27.groupby(['nombreinstitucion', 'cve_periodo', 'dat_id_credito_met_cnbv', 'cve_moneda']).agg(
        Número_de_Contratos_de_crédito_Vivienda=('cve_periodo', 'sum')
    ).reset_index()

    # Sumar 1000 a los valores de la columna 'Número_de_Contratos_de_crédito_Vivienda'
    df_combinado27['Número_de_Contratos_de_crédito_Vivienda'] += 1000

    # Eliminar duplicados en la columna 'nombreinstitucion'
    df_combinado27 = df_combinado27.drop_duplicates(subset=['nombreinstitucion'])
    
    
    
    
    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado27 = df_combinado27.groupby('nombreinstitucion').agg(
        Número_de_Contrato_de_crédito_Vivienda=('Número_de_Contratos_de_crédito_Vivienda', 'sum')
    ).reset_index()

    return df_combinado27
