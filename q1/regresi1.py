import matplotlib.pyplot as plt
from scipy import stats

x = [10,28,29,35,48,55,71,73,80,88,91,111,131,144,160]
y = [29,47,55,65,79,82,92,95,100,102,110,124,127,130,152]

slope, intercept, r, p, std_err = stats.linregress(x,y)

print('slope =', slope)
print('intercept =', intercept)

def myfunc(x):
  return intercept + slope * x

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()