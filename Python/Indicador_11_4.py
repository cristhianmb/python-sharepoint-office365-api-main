#Saldo de la Cartera de crédito con riesgo de crédito etapa 1+2 de Pymes
import pandas as pd


def Indicador_11_4(df_hoja9_1, df_hoja2):
    df18 = df_hoja9_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado36 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df18[['Institución', 'Cartera_etap1+etap2', 'Tamaño_de_empresa_calculado_ventas_50M', 'EstadoCalculado']], how='left', left_on='nombreinstitucion', right_on='Institución')

    # Agrupar y agregar según tus necesidades
    df_combinado36 = df_combinado36.groupby(['nombreinstitucion', 'claveinstitucion', 'Institución', 'Cartera_etap1+etap2', 'Tamaño_de_empresa_calculado_ventas_50M', 'EstadoCalculado']).agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa=('Cartera_etap1+etap2', 'mean')
    ).reset_index()

    # Filtrar el DataFrame para mostrar solo los datos "MiPyMEs" en 'Tamaño_de_empresa_calculado_ventas_50M'
    df_combinado36 = df_combinado36[df_combinado36['Tamaño_de_empresa_calculado_ventas_50M'] == 'MiPyMEs']

    # Filtrar el DataFrame para mostrar solo los datos "MiPyMEs" en 'Tamaño_de_empresa_calculado_ventas_50M'
    df_combinado36 = df_combinado36[df_combinado36['EstadoCalculado'] == 'MEXICO']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado36 = df_combinado36.groupby('nombreinstitucion').agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa=('Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa', 'mean')
    ).reset_index()

    return df_combinado36

