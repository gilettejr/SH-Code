import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

f = open('stars.txt','r')
lines = f.readlines()
stars = []
for i in lines:
	stars.append(float(i))
f.close()

f = open('rads.txt','r')
lines = f.readlines()
rads = []
for j in lines:
	rads.append(float(j))
f.close()

stars = np.array(stars)
rads = np.array(rads)

fit = np.polyfit(rads,stars,1)
fit_fn = np.poly1d(fit)



plt.plot(rads,stars, 'yo',label = linregress(rads,stars))
plt.xlabel('Distance of Region from Galactic Centre(Pixels)')
plt.ylabel('Stars in Region')
plt.legend()
plt.show()



	
