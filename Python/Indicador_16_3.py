#Saldo de Ingresos provenientes de operaciones de cobertura - 2021
import pandas as pd

def Indicador_16_3(df_combinado59, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    #valor_BQ1 = -10000000000

    df_combinado65 = df_combinado59.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado65['Saldo_de_Ingresos_provenientes_de_operaciones_de_cobertura'] = (
        df_combinado65['Saldo_de_Ingresos_provenientes_de_operaciones_de_cobertura'] - 2022
    ) * (1 + IPC) 

    return df_combinado65
