#saldo de inversiones en instrumentos financieros - 2021
import pandas as pd

def Indicador_17_2(df_combinado67, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    valor_BQ1 = 100000000

    df_combinado69 = df_combinado67.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado69['saldo_de_inversiones_en_instrumentos_financieros'] = (
        df_combinado69['saldo_de_inversiones_en_instrumentos_financieros'] - 2022
    ) * (1 + IPC) - (valor_BQ1)

    return df_combinado69
