#Saldo de comisiones por Alquiler de cajas de seguridad - 2022
import pandas as pd

def Indicador_17_12(df_hoja2_1, df_hoja2):
    df58 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado79 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df58[['importe_pesos', 'concepto', 'institucion']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado79 = df_combinado79.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_comisiones_por_Alquiler_de_cajas_de_seguridad=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado79 = df_combinado79[df_combinado79['concepto'] == 501000502060]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado79 = df_combinado79.groupby('nombreinstitucion').agg(
        Saldo_de_comisiones_por_Alquiler_de_cajas_de_seguridad=('Saldo_de_comisiones_por_Alquiler_de_cajas_de_seguridad', 'mean')
    ).reset_index()

    return df_combinado79
