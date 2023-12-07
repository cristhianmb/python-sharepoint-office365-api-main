#Saldo de Premios por colación de deuda - 2022
import pandas as pd

def Indicador_15_5(df_hoja2_1, df_hoja2):
    df44 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado61 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df44[['importe_pesos', 'concepto', 'institucion']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado61 = df_combinado61.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_Premios_por_colacion_de_deuda=('importe_pesos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado61 = df_combinado61[df_combinado61['concepto'] == 600400202025]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado61 = df_combinado61.groupby('nombreinstitucion').agg(
        Saldo_de_Premios_por_colacion_de_deuda=('Saldo_de_Premios_por_colacion_de_deuda', 'sum')
    ).reset_index()

    return df_combinado61
