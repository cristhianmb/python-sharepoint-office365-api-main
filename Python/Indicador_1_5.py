#Saldo de la Captaci—n Total - 2021
import pandas as pd

def Indicador_1_5(df_hoja1, df_hoja2):
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado10 = pd.merge(df_hoja1, df_hoja2[['claveinstitucion', 'nombreinstitucion']], how='left', left_on='institucion', right_on='claveinstitucion')
    df_combinado10 = df_combinado10.groupby(['nombreinstitucion', 'concepto']).agg(Saldo_de_la_Captación_Total=('importe_pesos', 'mean')).reset_index()
    df_combinado10 = df_combinado10[df_combinado10['concepto'] == 200200001001]
    
    

    IPC = 7.36 / 100
    #df_combinado10['indicador_1_1'] = df_combinado10['promedio'] * (1 + IPC)  
    df_combinado10['Saldo_de_la_Captación_Total'] = df_combinado10['Saldo_de_la_Captación_Total'] * (1 + IPC)  


    return df_combinado10
