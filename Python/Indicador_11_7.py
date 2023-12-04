#Saldo de la Cartera de crédito con riesgo de crédito etapa 3 de Empresa Grande
import pandas as pd



def Indicador_11_7(df_hoja9_1, df_hoja2):
    df21 = df_hoja9_1.copy()

    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado39 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']], df21[['Institución', 'EstadoCalculado', 'Tamaño_de_empresa_calculado_ventas_50M', 'Textbox2']], how='left', left_on='nombreinstitucion', right_on='Institución')

    # Agrupar y agregar según tus necesidades
    df_combinado39 = df_combinado39.groupby(['nombreinstitucion', 'claveinstitucion', 'Institución', 'Tamaño_de_empresa_calculado_ventas_50M', 'Textbox2', 'EstadoCalculado']).agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa=('Textbox2', 'mean')
    ).reset_index()

    # Filtrar el DataFrame para mostrar solo los datos "MiPyMEs" en 'Tamaño_de_empresa_calculado_ventas_50M'
    df_combinado39 = df_combinado39[df_combinado39['Tamaño_de_empresa_calculado_ventas_50M'] == 'Grande']

    # Filtrar el DataFrame para mostrar solo los datos "MiPyMEs" en 'Tamaño_de_empresa_calculado_ventas_50M'
    df_combinado39 = df_combinado39[df_combinado39['EstadoCalculado'] == 'MEXICO']

    # Realizar la agregación sin repetir los valores de 'nombreinstitucion'
    df_combinado39 = df_combinado39.groupby('nombreinstitucion').agg(
        Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa=('Saldo_de_la_Cartera_de_crédito_con_riesgo_de_crédito_etapa', 'mean')
    ).reset_index()

    return df_combinado39
