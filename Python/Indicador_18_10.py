#Saldo de comisiones por Servicios de banca electrónica - 2021
import pandas as pd

def Indicador_18_10(df_combinado80, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    # valor_BQ1 = 100000000

    df_combinado90 = df_combinado80.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado90['Saldo_de_comisiones_por_Servicios_de_banca_electronica'] = (
        df_combinado90['Saldo_de_comisiones_por_Servicios_de_banca_electronica'] - 2022
    ) * (1 + IPC) 

    return df_combinado90