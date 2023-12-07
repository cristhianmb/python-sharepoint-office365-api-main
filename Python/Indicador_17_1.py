#saldo de posiciones activas de instrumentos financieros derivados - 2022
import pandas as pd

def Indicador_17_1(df_hoja2_1, df_hoja2):
    df47 = df_hoja2_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado68 = pd.merge(
        df_hoja2[['nombreinstitucion', 'claveinstitucion']],
        df47[['importe_pesos', 'concepto', 'institucion']],
        how='left',
        left_on='claveinstitucion',
        right_on='institucion'
    )

    # Agrupar y agregar según tus necesidades
    df_combinado68 = df_combinado68.groupby(['nombreinstitucion', 'claveinstitucion', 'importe_pesos', 'concepto']).agg(
        saldo_de_posiciones_activas_de_instrumentos_financieros_derivados=('importe_pesos', 'mean')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado68 = df_combinado68[df_combinado68['concepto'] == 501407203061]

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado68 = df_combinado68.groupby('nombreinstitucion').agg(
        saldo_de_posiciones_activas_de_instrumentos_financieros_derivados=('saldo_de_posiciones_activas_de_instrumentos_financieros_derivados', 'mean')
    ).reset_index()

    return df_combinado68
