# Número de Contratos de crédito - Empresas - 2021
import pandas as pd

def Indicador_10_5(df_hoja8_1, df_hoja2):
    df14 = df_hoja8_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado32 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df14[['Créditos', 'Institución']], how='left', left_on='nombreinstitucion', right_on='Institución')

    # Agrupar y agregar según tus necesidades
    df_combinado32 = df_combinado32.groupby(['nombreinstitucion', 'claveinstitucion']).agg(
        Número_de_Contratos_de_crédito_Empresas=('Créditos', 'sum')
    ).reset_index()

    # Eliminación de columnas sobrantes
    columna_eliminar = ['claveinstitucion']
    df_combinado32 = df_combinado32.drop(columna_eliminar, axis=1)

    return df_combinado32
