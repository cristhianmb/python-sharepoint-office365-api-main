#Saldo de comisiones por Cartas de crédito sin refinanciamiento - 2022
import pandas as pd

def Indicador_17_6(df_hoja2_1, df_hoja2):
    df50 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado73 = pd.merge(
        df_hoja2[['nombreinstitucion', 'claveinstitucion']],
        df50[['importe_pesos', 'concepto', 'institucion']],
        how='left',
        left_on='claveinstitucion',
        right_on='institucion'
    )

    # Agrupar y agregar según tus necesidades
    df_combinado73 = df_combinado73.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_comisiones_por_Cartas_de_credito_sin_refinanciamiento=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado73 = df_combinado73[df_combinado73['concepto'] == 501000502048]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado73 = df_combinado73.groupby('nombreinstitucion').agg(
        Saldo_de_comisiones_por_Cartas_de_credito_sin_refinanciamiento=('Saldo_de_comisiones_por_Cartas_de_credito_sin_refinanciamiento', 'mean')
    ).reset_index()

    return df_combinado73
