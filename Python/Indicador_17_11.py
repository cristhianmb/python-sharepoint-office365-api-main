#Saldo de comisiones por Custodia o administración de bienes - 2022
import pandas as pd

def Indicador_17_11(df_hoja2_1, df_hoja2):
    df57 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado78 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df57[['importe_pesos', 'concepto', 'institucion']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado78 = df_combinado78.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_comisiones_por_Custodia_o_administracion_de_bienes=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado78 = df_combinado78[df_combinado78['concepto'] == 501000502059]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado78 = df_combinado78.groupby('nombreinstitucion').agg(
        Saldo_de_comisiones_por_Custodia_o_administracion_de_bienes=('Saldo_de_comisiones_por_Custodia_o_administracion_de_bienes', 'mean')
    ).reset_index()

    return df_combinado78
