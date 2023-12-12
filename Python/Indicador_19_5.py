#número de Terminales Punto de Venta - 2022
import pandas as pd

def Indicador_19_5(df_hoja11_1, df_hoja2_1, df_hoja2):
    # Codigo de prueba con calculos ya utilizados en el programa
    df65 = df_hoja11_1.copy()

    # Eliminar los dos últimos dígitos numéricos en la columna 'Año'
    df65['Column1'] = df65['Column1'] // 100
    
    # Combinar DataFrames en 'institucion' y 'claveinstitucion'
    df_combinado97 = pd.merge(df_hoja2[['nombreinstitucion', 'claveinstitucion']],
                              df65[['Column1','Column4', 'Column10']],
                              how='left',
                              left_on='claveinstitucion',
                              right_on='Column4')

    # Agrupar y agregar según tus necesidades
    df_combinado97 = df_combinado97.groupby(['nombreinstitucion', 'claveinstitucion', 'Column10', 'Column1']).agg(
        numero_de_Terminales_Punto_de_Venta=('Column10', 'count')
    ).reset_index()

    # Filtrar por el periodo deseado (2022)
    df_combinado97 = df_combinado97[df_combinado97['Column1'] == 2022]
    df_combinado97 = df_combinado97[df_combinado97['Column10'] == 'TPV']

    # Eliminación de columnas sobrantes
    columna_eliminar = ['Column10', 'claveinstitucion', 'Column1']
    df_combinado97 = df_combinado97.drop(columna_eliminar, axis=1)

    return df_combinado97
