#Saldo de comisiones por Cheques de caja - 2021
import pandas as pd

def Indicador_18_6(df_combinado76, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    # valor_BQ1 = 100000000

    df_combinado86 = df_combinado76.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado86['Saldo_de_comisiones_por_Cheques_de_caja'] = (
        df_combinado86['Saldo_de_comisiones_por_Cheques_de_caja'] - 2022
    ) * (1 + IPC) 

    return df_combinado86
