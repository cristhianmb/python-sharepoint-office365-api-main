#Saldo de comisiones por Cartas de crédito sin refinanciamiento - 2021
import pandas as pd

def Indicador_18_3(df_combinado73, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    # valor_BQ1 = 100000000

    df_combinado83 = df_combinado73.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado83['Saldo_de_comisiones_por_Cartas_de_credito_sin_refinanciamiento'] = (
        df_combinado83['Saldo_de_comisiones_por_Cartas_de_credito_sin_refinanciamiento'] - 2022
    ) * (1 + IPC) 

    return df_combinado83

