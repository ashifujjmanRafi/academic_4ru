import numpy as np
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print(np.mean(speed))
print(np.median(speed))
# from scipy import stats
# print(stats.mode(speed))
print(np.std(speed))

#create random data
#dataset
ds = np.random.uniform(1,5,1000)

#histogram
plt.hist(ds)
plt.savefig('histogram.png')
plt.show()