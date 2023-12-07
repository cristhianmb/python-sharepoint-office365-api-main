#Saldo de Resultado por compra-venta de instrumentos financieros e instrumentos financieros derivados - 2022
import pandas as pd

def Indicador_15_6(df_hoja2_1, df_hoja2):
    df45 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado62 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df45[['importe_pesos', 'concepto', 'institucion']], how='left', left_on='claveinstitucion', right_on='institucion')

    # Agrupar y agregar según tus necesidades
    df_combinado62 = df_combinado62.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        Saldo_de_Resultado_por_compra_venta_de_instrumentos_financieros_e_instrumentos_financieros_derivados=('importe_pesos', 'sum')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado62 = df_combinado62[df_combinado62['concepto'] == 501400702077]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado62 = df_combinado62.groupby('nombreinstitucion').agg(
        Saldo_de_Resultado_por_compra_venta_de_instrumentos_financieros_e_instrumentos_financieros_derivados=('Saldo_de_Resultado_por_compra_venta_de_instrumentos_financieros_e_instrumentos_financieros_derivados', 'sum')
    ).reset_index()

    return df_combinado62
