import pandas as pd
csvFile = r"F:\Users\jcportilla\python-csv\activities.csv"
df_actividades = pd.read_csv(csvFile, delimiter=',')
print(df_actividades.head())