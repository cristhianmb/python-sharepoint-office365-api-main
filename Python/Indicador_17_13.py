#Saldo de comisiones por Servicios de banca electrónica - 2022
import pandas as pd

def Indicador_17_13(df_hoja2_1, df_hoja2):
    df59 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado80 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df59[['importe_pesos', 'concepto', 'institucion']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado80 = df_combinado80.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_comisiones_por_Servicios_de_banca_electronica=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado80 = df_combinado80[df_combinado80['concepto'] == 501000502061]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado80 = df_combinado80.groupby('nombreinstitucion').agg(
        Saldo_de_comisiones_por_Servicios_de_banca_electronica=('Saldo_de_comisiones_por_Servicios_de_banca_electronica', 'mean')
    ).reset_index()

    return df_combinado80
