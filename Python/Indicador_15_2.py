#Saldo de intereses y rendimientos a favor en operaciones de reportos - 2022
import pandas as pd

def Indicador_15_2(df_hoja2_1, df_hoja2):
    df40 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado58 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df40[['importe_pesos', 'concepto', 'institucion']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado58 = df_combinado58.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_intereses_y_rendimientos_a_favor_en_operaciones_de_reportos=('importe_pesos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado58 = df_combinado58[df_combinado58['concepto'] == 500200102005]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado58 = df_combinado58.groupby('nombreinstitucion').agg(
        Saldo_de_intereses_y_rendimientos_a_favor_en_operaciones_de_reportos=('Saldo_de_intereses_y_rendimientos_a_favor_en_operaciones_de_reportos', 'sum')
    ).reset_index()

    return df_combinado58
