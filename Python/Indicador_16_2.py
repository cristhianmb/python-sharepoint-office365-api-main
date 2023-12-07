#Saldo de intereses y rendimientos a favor en operaciones de reportos - 2021
import pandas as pd

def Indicador_16_2(df_combinado58, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    #valor_BQ1 = -10000000000

    df_combinado64 = df_combinado58.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado64['Saldo_de_intereses_y_rendimientos_a_favor_en_operaciones_de_reportos'] = (
        df_combinado64['Saldo_de_intereses_y_rendimientos_a_favor_en_operaciones_de_reportos'] - 2022
    ) * (1 + IPC)

    return df_combinado64
