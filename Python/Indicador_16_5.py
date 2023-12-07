#saldo de inversiones en instrumentos financieros - 2022
import pandas as pd

def Indicador_16_5(df_hoja2_1, df_hoja2):
    df46 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado67 = pd.merge(
        df_hoja2[['nombreinstitucion', 'claveinstitucion']],
        df46[['importe_pesos', 'concepto', 'institucion']],
        how='left',
        left_on='claveinstitucion',
        right_on='institucion'
    )

    # Agrupar y agregar según tus necesidades
    df_combinado67 = df_combinado67.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        saldo_de_inversiones_en_instrumentos_financieros=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado67 = df_combinado67[df_combinado67['concepto'] == 501000502050]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado67 = df_combinado67.groupby('nombreinstitucion').agg(
        saldo_de_inversiones_en_instrumentos_financieros=('saldo_de_inversiones_en_instrumentos_financieros', 'mean')
    ).reset_index()

    return df_combinado67
