#Saldo de Ingresos provenientes de operaciones de cobertura - 2022
import pandas as pd

def Indicador_15_3(df_hoja2_1, df_hoja2):
    df41 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado59 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df41[['importe_pesos', 'concepto', 'institucion']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado59 = df_combinado59.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_Ingresos_provenientes_de_operaciones_de_cobertura=('importe_pesos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado59 = df_combinado59[df_combinado59['concepto'] == 500200102006]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado59 = df_combinado59.groupby('nombreinstitucion').agg(
        Saldo_de_Ingresos_provenientes_de_operaciones_de_cobertura=('Saldo_de_Ingresos_provenientes_de_operaciones_de_cobertura', 'sum')
    ).reset_index()

    return df_combinado59
