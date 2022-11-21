import numpy as np
import matplotlib.pyplot as plt 

xf = np.random.randint(0,1000)
yf = np.random.randint(0,1000)
xb = np.random.randint(0,1000)
yb = np.random.randint(0,1000)

fcx = []
fcy = []
bcx = []
bcy = []

fcx.append(xf)
fcy.append(yf)
bcx.append(xb)
bcy.append(yb)

caught = False
v = 20
t = 0
while True:
    
    d = np.sqrt((xf-xb)**2 + (yf-yb)**2)
    if(d<100):
        caught = True
        break
    elif(d>900):
        caught = False
        break
    t += 1
    xf += v*(xb - xf)/d
    yf += v*(yb -yf)/d

    xb = np.random.randint(0,1000)
    yb = np.random.randint(0,1000)

    fcx.append(xf)
    fcy.append(yf)
    bcx.append(xb)
    bcy.append(yb)

print("bomber caught",caught)
print("at time ",t)
plt.plot(fcx,fcy,'red')
plt.plot(bcx,bcy,'blue')
plt.show()
