import pandas as pd
import json 

csvFile = "/home/vk/Documents/csvreader/activities.csv"
df_actividades = pd.read_csv(csvFile, delimiter=',')

# Check for 'ANOMALIA' or 'VISITA' in uppercase and tag as 'anomalia', 'visita' or 'normalizacion'
df_actividades['activities_normalized'] = df_actividades['Actividad'].apply(lambda x: 'anomalia' if ('ANOMALIA' in x or 'LINEA' in x)  else 
                                         ('visita' if 'VISITA' in x else 'normalizacion'))
df_actividades['datetime'] = pd.to_datetime(df_actividades['Ejecucion'], errors='coerce')

# Extract month and create a new column 'mes'
df_actividades['mes'] = df_actividades['datetime'].dt.month
counts = df_actividades.groupby(['mes', 'Contrato']).size().reset_index(name='count')
print (counts)
contract_to_city = {
      "DIC 209.2023":"Tumaco",
      "P Y 242.2023":"Pie de Monte",
      "MEC 289.2024": "Tumaco AMI",
      "ELE 283.2024" :"Tumaco",
      "VIL 350.2024" :"Pie de Monte"
}
df_actividades['city'] = df_actividades['Contrato'].map(contract_to_city)
df_april = df_actividades[df_actividades['mes'] == 5]
activity_counts = df_actividades.groupby(['city', 'activities_normalized']).size().reset_index(name='count')
print(activity_counts)

city_activity_dict = activity_counts.groupby('city')['count'].apply(list).to_dict()

# Display the dictionary
print("\nDictionary of counts by city:")
print(city_activity_dict)

# Convert the dictionary to a JSON string
city_activity_json = json.dumps(city_activity_dict)

act_counts_by_month = df_actividades.groupby(['mes', 'activities_normalized']).size().reset_index(name='count')
pivot_df = act_counts_by_month.pivot(index='mes', columns='activities_normalized', values='count').fillna(0).reset_index()

result = {}
for activity in pivot_df.columns[1:]:  # Skip the 'month' column
    result[activity] = list(pivot_df[activity].astype(int))

by_month_json = json.dumps(result, indent=4)
print(by_month_json)
print(act_counts_by_month)
# Display the JSON string
print("\nJSON string of counts by city:")
print(city_activity_json)
