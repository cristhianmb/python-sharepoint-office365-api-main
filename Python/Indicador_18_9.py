#Saldo de comisiones por Alquiler de cajas de seguridad - 2021
import pandas as pd

def Indicador_18_9(df_combinado79, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    # valor_BQ1 = 100000000

    df_combinado89 = df_combinado79.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado89['Saldo_de_comisiones_por_Alquiler_de_cajas_de_seguridad'] = (
        df_combinado89['Saldo_de_comisiones_por_Alquiler_de_cajas_de_seguridad'] - 2022
    ) * (1 + IPC) 

    return df_combinado89
