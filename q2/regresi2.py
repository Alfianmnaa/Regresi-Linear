import matplotlib.pyplot as plt
from scipy import stats

x = [1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]
y = [245,312,279,308,199,219,405,324,319,255]

slope, intercept, r, p, std_err = stats.linregress(x,y)

print('slope =', slope)
print('intercept =', intercept)

def myfunc(x):
  return intercept + slope * x

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()