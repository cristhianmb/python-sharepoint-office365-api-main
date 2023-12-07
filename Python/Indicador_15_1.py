#Saldo de Intereses y rendimientos a favor provenientes de inversiones en instrumentos financieros - 2022

import pandas as pd

def Indicador_15_1(df_hoja2_1, df_hoja2):
    df39 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado57 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df39[['importe_pesos', 'concepto', 'institucion']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado57 = df_combinado57.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros=('importe_pesos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado57 = df_combinado57[df_combinado57['concepto'] == 500200102004]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado57 = df_combinado57.groupby('nombreinstitucion').agg(
        Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros=('Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros', 'sum')
    ).reset_index()

    return df_combinado57
