#Saldo de comisiones por Giros bancarios - 2021
import pandas as pd

def Indicador_18_5(df_combinado75, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    # valor_BQ1 = 100000000

    df_combinado85 = df_combinado75.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado85['Saldo_de_comisiones_por_Giros_bancarios'] = (
        df_combinado85['Saldo_de_comisiones_por_Giros_bancarios'] - 2022
    ) * (1 + IPC) 

    return df_combinado85
