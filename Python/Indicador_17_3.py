#saldo de posiciones activas de instrumentos financieros derivados - 2021
import pandas as pd

def Indicador_17_3(df_combinado68, df_hoja2_1, df_hoja2):
    IPC = 7.36 / 100
    #valor_BQ1 = 100000000

    df_combinado70 = df_combinado68.copy()

    # Aplicar la fórmula a la columna 'Saldo_de_Intereses_y_rendimientos_a_favor_provenientes_de_inversiones_en_instrumentos_financieros'
    df_combinado70['saldo_de_posiciones_activas_de_instrumentos_financieros_derivados'] = (
        df_combinado70['saldo_de_posiciones_activas_de_instrumentos_financieros_derivados'] - 2022
    ) * (1 + IPC)

    return df_combinado70
