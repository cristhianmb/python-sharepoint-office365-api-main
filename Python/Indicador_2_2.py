#Ingresos de cartera de crédito con riesgo de crédito etapa 2 - 2022
import pandas as pd

def Indicador_2_2(df_hoja1, hoja2_1):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado12 = pd.merge(df_hoja1, hoja2_1[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado12 = df_combinado12.groupby(['nombreinstitucion', 'concepto']).agg(Ingresos_de_cartera_de_crédito_con_riesgo_de_crédito_etapa=('importe_pesos', 'sum')).reset_index()
    df_combinado12 = df_combinado12[df_combinado12['concepto'] == 500200102009]
    
    
    
    
    # Eliminación de columnas sobrantes
    columna_eliminar = ['concepto']
    df_combinado12=df_combinado12.drop(columna_eliminar,axis = 1)
    
    return df_combinado12


