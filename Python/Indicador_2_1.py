#Saldo de la Captaci—n Total - 2021
import pandas as pd

def Indicador_2_1(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado11 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado11 = df_combinado11.groupby(['nombreinstitucion', 'concepto']).agg(Ingresos_por_Intereses_de_Cartera_de_crédito_con_riesgo_de_crédito_etapa=('importe_pesos', 'sum')).reset_index()
    df_combinado11 = df_combinado11[df_combinado11['concepto'] == 500200102008]
    
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto']
    df_combinado11=df_combinado11.drop(columna_eliminar,axis = 1)
    
    return df_combinado11


