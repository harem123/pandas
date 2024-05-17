import pandas as pd
csvFile = r"F:\Users\jcportilla\python-csv\activities.csv"
df_actividades = pd.read_csv(csvFile, delimiter=',')


# Example DataFrame



# Check for 'ANOMALIA' or 'VISITA' in uppercase and tag as 'anomalia', 'visita' or 'normalizacion'
df_actividades['activities_normalized'] = df_actividades['Actividad'].apply(lambda x: 'anomalia' if ('ANOMALIA' in x or 'LINEA' in x)  else 
                                         ('visita' if 'VISITA' in x else 'normalizacion'))

print(df_actividades.head())
