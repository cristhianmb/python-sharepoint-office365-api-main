#Saldo de comisiones por Cheques de caja - 2022
import pandas as pd

def Indicador_17_9(df_hoja2_1, df_hoja2):
    df54 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado76 = pd.merge(
        df_hoja2[['nombreinstitucion', 'claveinstitucion']],
        df54[['importe_pesos', 'concepto', 'institucion']],
        how='left',
        left_on='claveinstitucion',
        right_on='institucion'
    )

    # Agrupar y agregar según tus necesidades
    df_combinado76 = df_combinado76.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_comisiones_por_Cheques_de_caja=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado76 = df_combinado76[df_combinado76['concepto'] == 501000502056]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado76 = df_combinado76.groupby('nombreinstitucion').agg(
        Saldo_de_comisiones_por_Cheques_de_caja=('Saldo_de_comisiones_por_Cheques_de_caja', 'mean')
    ).reset_index()

    return df_combinado76
