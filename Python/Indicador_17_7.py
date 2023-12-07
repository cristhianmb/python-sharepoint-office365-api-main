#Saldo de comisiones por Transferencia de fondos - 2022
import pandas as pd

def Indicador_17_7(df_hoja2_1, df_hoja2):
    df52 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado74 = pd.merge(
        df_hoja2[['nombreinstitucion', 'claveinstitucion']],
        df52[['importe_pesos', 'concepto', 'institucion']],
        how='left',
        left_on='claveinstitucion',
        right_on='institucion'
    )

    # Agrupar y agregar según tus necesidades
    df_combinado74 = df_combinado74.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_comisiones_por_Transferencia_de_fondos=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado74 = df_combinado74[df_combinado74['concepto'] == 501000502054]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado74 = df_combinado74.groupby('nombreinstitucion').agg(
        Saldo_de_comisiones_por_Transferencia_de_fondos=('Saldo_de_comisiones_por_Transferencia_de_fondos', 'mean')
    ).reset_index()

    return df_combinado74
