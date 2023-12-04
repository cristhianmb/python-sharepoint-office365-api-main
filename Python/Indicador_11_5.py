#Saldo de la Cartera de crédito con riesgo de crédito etapa 3 de Pymes
import pandas as pd


def Indicador_11_5(df_hoja9_1, df_hoja2):
    df19 = df_hoja9_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado37 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df19[['Institución', 'EstadoCalculado', 'Tamaño_de_empresa_calculado_ventas_50M', 'Textbox2']], how='left', left_on='nombreinstitucion', right_on='Institución')

    # Agrupar y agregar según tus necesidades
    df_combinado37 = df_combinado37.groupby(['nombreinstitucion', 'claveinstitucion', 'Institución', 'Textbox2', 'Tamaño_de_empresa_calculado_ventas_50M', 'EstadoCalculado']).agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa=('Textbox2', 'mean')
    ).reset_index()

    # Filtrar el DataFrame para mostrar solo los datos "MiPyMEs" en 'Tamaño_de_empresa_calculado_ventas_50M'
    df_combinado37 = df_combinado37[df_combinado37['Tamaño_de_empresa_calculado_ventas_50M'] == 'MiPyMEs']

    # Filtrar el DataFrame para mostrar solo los datos "MiPyMEs" en 'Tamaño_de_empresa_calculado_ventas_50M'
    df_combinado37 = df_combinado37[df_combinado37['EstadoCalculado'] == 'MEXICO']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado37 = df_combinado37.groupby('nombreinstitucion').agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa=('Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa', 'mean')
    ).reset_index()

    return df_combinado37
