import pandas as pd
csvFile = r"F:\Users\jcportilla\python-csv\activities.csv"
df_actividades = pd.read_csv(csvFile, delimiter=',')

# Check for 'ANOMALIA' or 'VISITA' in uppercase and tag as 'anomalia', 'visita' or 'normalizacion'
df_actividades['activities_normalized'] = df_actividades['Actividad'].apply(lambda x: 'anomalia' if ('ANOMALIA' in x or 'LINEA' in x)  else 
                                         ('visita' if 'VISITA' in x else 'normalizacion'))
df_actividades['datetime'] = pd.to_datetime(df_actividades['Ejecucion'], errors='coerce')

# Extract month and create a new column 'mes'
df_actividades['mes'] = df_actividades['datetime'].dt.month
counts = df_actividades.groupby(['mes', 'Contrato']).size().reset_index(name='count')

print(counts)
