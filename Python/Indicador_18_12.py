#Saldo del Resultado por compraventa de divisas - 2021
import pandas as pd

def Indicador_18_12(df_combinado91, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    # valor_BQ1 = 100000000

    df_combinado92 = df_combinado91.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado92['Saldo_del_Resultado_por_compraventa_de_divisas'] = (
        df_combinado92['Saldo_del_Resultado_por_compraventa_de_divisas'] - 2022
    ) * (1 + IPC) 

    return df_combinado92
