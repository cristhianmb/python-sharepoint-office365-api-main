#Saldo de Premios a favor en operaciones de préstamo de valores - 2022
import pandas as pd

def Indicador_15_4(df_hoja2_1, df_hoja2):
    df43 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado60 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df43[['importe_pesos', 'concepto', 'institucion']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado60 = df_combinado60.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_Premios_a_favor_en_operaciones_de_prestamo_de_valores=('importe_pesos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado60 = df_combinado60[df_combinado60['concepto'] == 500200102015]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado60 = df_combinado60.groupby('nombreinstitucion').agg(
        Saldo_de_Premios_a_favor_en_operaciones_de_prestamo_de_valores=('Saldo_de_Premios_a_favor_en_operaciones_de_prestamo_de_valores', 'sum')
    ).reset_index()

    return df_combinado60
