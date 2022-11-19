import random as rd
import matplotlib.pyplot as plt
import numpy as np

xb = rd.randint(0,1000)
yb = rd.randint(0,1000)

xf = rd.randint(0,1000)
yf = rd.randint(0,1000)

v = 20
t = 0

fcx = []
fcy = []
bcx = []
bcy = []
fcx.append(xf)
fcy.append(yf)
bcx.append(xb)
bcy.append(yb)
caught = False
while True:
    distance = np.sqrt((xb-xf)**2+(yb-yf)**2)
    if(distance<100):
        caught = True
        break
    elif distance>900:
        caught = False
    t += 1
    xf = xf+ v*(xb-xf)/distance
    yf = yf+ v*(yb-yf)/distance

    fcx.append(xf)
    fcy.append(yf)

    xb = rd.randint(0,1000)
    yb = rd.randint(0,1000)

    bcx.append(xb)
    bcy.append(yb)

plt.plot(fcx,fcy,'red')
plt.plot(bcx,bcy)

print("The fighter is cought: ", caught)

plt.show()


print(t)