import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib as mpl

df = pd.read_csv("q4/data3.csv")
reg = LinearRegression()
reg.fit(df[['Volume','Weight']].values,df.CO2)

mpl.rcParams['legend.fontsize'] = 12
fig = plt.figure()
ax = fig.add_subplot(projection ='3d')
ax.scatter(df.Volume, df.Weight, df.CO2)
ax.legend()
ax.view_init(45, 0)
plt.show()

a = reg.coef_
b = reg.intercept_

X_baru = np.array([8, 125]).reshape(-1, 2)
prediksi_CO2 = reg.predict(X_baru)

print('Koefisien regresi = ', a[0],'dan', a[1])
print('Intercept = ', b)
print('Hasil prediksi untuk Volume=8 dan Weight=125 yaitu', prediksi_CO2)