import pandas as pd
#A
dict = {'CP':[6230,2128,3180,3360,5600],
        "CA": [3388,3402,3454,3755,260],
        'Localidad':['General Villegas','Arroyo Seco','Federal','Oberá','San Rafael']}
#B
df = pd.DataFrame(dict)
#C.i
df_ord = df.sort_values(by=["Localidad"])
#C.ii
cp_mas_alto =df['CP'].max()
#C.iii
ca_mas_bajo = df["CA"].min()
#C.iv
df["CP-CA"] = abs(df["CP"]-df["CA"])
df_ord_cp_ca = df.sort_values(by=["CP-CA"])
a = df_ord_cp_ca["Localidad"][0:1].to_string(index = False)
#C.v
promedio_cp = df["CP"].mean()
#C.vi
sumatoria_ca = df["CA"].sum()
#C.vii
ca_menores_3500 = df[df["CA"]<3500].values
for i in range(len(ca_menores_3500)):
        print(ca_menores_3500[i][2])
print()
#C.viii
ca_menores_3500 = df[df["CP"]>3500].values
for i in range(len(ca_menores_3500)):
        print(ca_menores_3500[i][2])
#D
df_ord.to_csv("localidades.csv",index=False)