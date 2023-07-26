import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("1_visualizacions_Cinear_Play - Hoja 1.csv")

#A
cant_visualizaciones_totales = df["visualizaciones_totales"].sum()
# print(cant_visualizaciones_totales)

#B
#Convertir string de fecha en datetime
df['indice_tiempo'] = pd.to_datetime(df['indice_tiempo'])
#Agrupar las horas vistas por año y calcular el promedio de cada año
grouped_data = df.groupby(pd.Grouper(key='indice_tiempo', freq='Y'))['total_horas_vistas'].mean()
# print(grouped_data)
grouped_data_ord = grouped_data.sort_values(ascending=False)
# print(grouped_data_ord[0:1])

#C
df_sort_desc_cant_visual = df.sort_values(by="visualizaciones_totales",ascending=False)
fecha_max_visualizaciones = df_sort_desc_cant_visual["indice_tiempo"][0:1].to_string()[2:]
# print(fecha_max_visualizaciones)

#D
may_2022 = int(df.loc[df['indice_tiempo'] == '2022-05-01']['visualizaciones_totales'])
may_2020 = int(df.loc[df['indice_tiempo'] == '2020-05-01']['visualizaciones_totales'])
variacion_porcentual = round((may_2022 - may_2020)/may_2020*100,2)
#print(variacion_porcentual)

#E
df.plot.line(x="indice_tiempo",y="visualizaciones_totales")
plt.show()