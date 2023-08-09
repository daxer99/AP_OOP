import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("2_Centrales_generacion_electrica - Hoja 1.csv")

#A
data_a = data.groupby(['provincia'])['provincia'].count()
data_a = data_a.sort_values(ascending=False)
#print(data_a.to_frame())

#B
data_b = data.groupby(['provincia'])['potencia_instalada_mw'].sum()
data_b = data_b.sort_values(ascending=False)
#print(data_b.to_frame())

#C
data_c = data.groupby(['tipo_tecnologia'])['potencia_instalada_mw'].sum()
data_c = data_c.sort_values(ascending=False)
#print(data_c.to_frame())

#D
cantidad_nan = data['potencia_instalada_mw'].isna().sum()
#print(cantidad_nan)

data["potencia_instalada_mw"] = data["potencia_instalada_mw"].fillna(0)

#E
#data_b.plot.bar(legend=True)
data_c.plot.bar(legend=True)
plt.show()