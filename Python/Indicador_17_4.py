#Saldo acumulado de Comisiones y Tarifas Cobradas - 2022
import pandas as pd

def Indicador_17_4(df_hoja2_1, df_hoja2):
    df48 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado71 = pd.merge(
        df_hoja2[['nombreinstitucion', 'claveinstitucion']],
        df48[['importe_pesos', 'concepto', 'institucion']],
        how='left',
        left_on='claveinstitucion',
        right_on='institucion'
    )

    # Agrupar y agregar según tus necesidades
    df_combinado71 = df_combinado71.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_acumulado_de_Comisiones_y_Tarifas_Cobradas=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado71 = df_combinado71[df_combinado71['concepto'] == 501000301005]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado71 = df_combinado71.groupby('nombreinstitucion').agg(
        Saldo_acumulado_de_Comisiones_y_Tarifas_Cobradas=('Saldo_acumulado_de_Comisiones_y_Tarifas_Cobradas', 'mean')
    ).reset_index()

    return df_combinado71
