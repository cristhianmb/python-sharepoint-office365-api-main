#Número de Contratos de crédito - Vivienda
import pandas as pd


def Indicador_4_1(df_hoja4_1, df_hoja2):
    df4 = df_hoja4_1.copy()
    # Eliminar los dos últimos dígitos numéricos en la columna 'cve_period
    df4['cve_periodo'] = df4['cve_periodo'] // 100

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado22 = pd.merge(df_hoja2[['nombreinstitucion','claveinstitucion']], df4[['cve_periodo', 'cve_institucion','creditos']], how='left', left_on='claveinstitucion', right_on='cve_institucion')
    
    # Agrupar y agregar según tus necesidades
    df_combinado22 = df_combinado22.groupby(['nombreinstitucion', 'cve_periodo', 'creditos']).agg(
        Número_de_Contratos_de_crédito_Nómina=('creditos', 'sum')
        ).reset_index()
    df_combinado22 = df_combinado22[df_combinado22['cve_periodo'] == 2022]

# Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado22 = df_combinado22.groupby('nombreinstitucion').agg(
        Número_de_Contratos_de_crédito_Nómina=('Número_de_Contratos_de_crédito_Nómina', 'sum')).reset_index()
    
    return df_combinado22
