#Saldo de comisiones por Giros bancarios - 2022
import pandas as pd

def Indicador_17_8(df_hoja2_1, df_hoja2):
    df56 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado75 = pd.merge(
        df_hoja2[['nombreinstitucion', 'claveinstitucion']],
        df56[['importe_pesos', 'concepto', 'institucion']],
        how='left',
        left_on='claveinstitucion',
        right_on='institucion'
    )

    # Agrupar y agregar según tus necesidades
    df_combinado75 = df_combinado75.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_comisiones_por_Giros_bancarios=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado75 = df_combinado75[df_combinado75['concepto'] == 501000502055]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado75 = df_combinado75.groupby('nombreinstitucion').agg(
        Saldo_de_comisiones_por_Giros_bancarios=('Saldo_de_comisiones_por_Giros_bancarios', 'mean')
    ).reset_index()

    return df_combinado75
