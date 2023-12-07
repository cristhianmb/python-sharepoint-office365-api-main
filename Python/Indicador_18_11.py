#Saldo del Resultado por compraventa de divisas - 2022
import pandas as pd

def Indicador_18_11(df_hoja2_1, df_hoja2):
    df60 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado91 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df60[['importe_pesos', 'concepto', 'institucion']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado91 = df_combinado91.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_del_Resultado_por_compraventa_de_divisas=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado91 = df_combinado91[df_combinado91['concepto'] == 501400702079]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado91 = df_combinado91.groupby('nombreinstitucion').agg(
        Saldo_del_Resultado_por_compraventa_de_divisas=('Saldo_del_Resultado_por_compraventa_de_divisas', 'mean')
    ).reset_index()

    return df_combinado91
