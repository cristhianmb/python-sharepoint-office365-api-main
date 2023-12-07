#Saldo de comisiones por Operaciones de Crédito - 2022
import pandas as pd

def Indicador_17_5(df_hoja2_1, df_hoja2):
    df49 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado72 = pd.merge(
        df_hoja2[['nombreinstitucion', 'claveinstitucion']],
        df49[['importe_pesos', 'concepto', 'institucion']],
        how='left',
        left_on='claveinstitucion',
        right_on='institucion'
    )

    # Agrupar y agregar según tus necesidades
    df_combinado72 = df_combinado72.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_comisiones_por_Operaciones_de_Credito=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado72 = df_combinado72[df_combinado72['concepto'] == 501000502045]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado72 = df_combinado72.groupby('nombreinstitucion').agg(
        Saldo_de_comisiones_por_Operaciones_de_Credito=('Saldo_de_comisiones_por_Operaciones_de_Credito', 'mean')
    ).reset_index()

    return df_combinado72
