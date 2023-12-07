#Saldo de Resultado por compra-venta de instrumentos financieros e instrumentos financieros derivados - 2021
import pandas as pd

def Indicador_16_4(df_combinado62, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    #valor_BQ1 = -10000000000

    df_combinado66 = df_combinado62.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado66['Saldo_de_Resultado_por_compra_venta_de_instrumentos_financieros_e_instrumentos_financieros_derivados'] = (
        df_combinado66['Saldo_de_Resultado_por_compra_venta_de_instrumentos_financieros_e_instrumentos_financieros_derivados'] - 2022
    ) * (1 + IPC) 

    return df_combinado66
