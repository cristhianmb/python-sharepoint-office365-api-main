#Saldo acumulado de Comisiones y Tarifas Cobradas - 2021
import pandas as pd

def Indicador_18_1(df_combinado71, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    # valor_BQ1 = 100000000

    df_combinado81 = df_combinado71.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado81['Saldo_acumulado_de_Comisiones_y_Tarifas_Cobradas'] = (
        df_combinado81['Saldo_acumulado_de_Comisiones_y_Tarifas_Cobradas'] - 2022
    ) * (1 + IPC) 

    return df_combinado81

