#Saldo de Intereses y rendimientos a favor provenientes de inversiones en instrumentos financieros - 2021
import pandas as pd

def Indicador_16_1(df_combinado57, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    valor_BQ1 = -10000000000

    df_combinado63 = df_combinado57.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado63['Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'] = (
        df_combinado63['Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'] - 2022
    ) * (1 + IPC) - valor_BQ1

    return df_combinado63


