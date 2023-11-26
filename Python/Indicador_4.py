#Saldo de la Cartera de créditos interbancarios con riesgo de crédito etapa 1 - 2022
import pandas as pd

def Indicador_4(df_hoja1, df_hoja2):
    
    df_combinado4 = pd.merge(df_hoja1, df_hoja2[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado4 = df_combinado4.groupby(['nombreinstitucion', 'concepto']).agg(Saldo_de_la_Cartera_de_créditos_interbancarios_con_riesgo_de_crédito_etapa=('importe_pesos', 'mean')).reset_index()
    df_combinado4 = df_combinado4[df_combinado4['concepto'] == 101800208009]
    
 

    return df_combinado4
