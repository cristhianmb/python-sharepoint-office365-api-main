#Número de Contratos de crédito - Empresas - 2022
import pandas as pd

def Indicador_8_1(df_hoja8_1, df_hoja2):
    # Número de Contratos de crédito - Empresas - 2022
    df8 = df_hoja8_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_periodo'
    df8['Periodo_seguimiento'] = pd.to_datetime(df8['Periodo_seguimiento']).dt.year
    df8['Periodo_seguimiento'] = pd.to_numeric(df8['Periodo_seguimiento'], errors='coerce')

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado26 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df8[['Periodo_seguimiento', 'Institución', 'Créditos']], how='left', left_on='nombreinstitucion', right_on='Institución')

    # Eliminar las columnas no deseadas
    columnas_a_eliminar = ['cve_periodo', 'dat_id_credito_met_cnbv', 'cve_moneda']
    df_combinado26 = df_combinado26.drop(columnas_a_eliminar, axis=1, errors='ignore')

    # Agrupar y agregar según tus necesidades
    df_combinado26 = df_combinado26.groupby(['nombreinstitucion', 'Periodo_seguimiento', 'Créditos']).agg(
        Número_de_Contratos_de_crédito_Empresas=('Créditos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado26 = df_combinado26[df_combinado26['Periodo_seguimiento'] == 2022]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado26 = df_combinado26.groupby('nombreinstitucion').agg(
        Número_de_Contrato_de_crédito_Empresas=('Número_de_Contratos_de_crédito_Empresas', 'sum')
    ).reset_index()

    return df_combinado26
