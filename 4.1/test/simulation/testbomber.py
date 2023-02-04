import numpy as np 
import matplotlib.pyplot as plt

xf = np.random.randint(0,1000)
yf = np.random.randint(0,1000)
xb =np.random.randint(0,1000)
yb = np.random.randint(0,1000)

fcx = []
fcy = []
bcx = []
bcy = []

fcx.append(xf)
fcy.append(yf)
bcx.append(xb)
bcy.append(yb)

t = 0
v = 20
caught = False

while True :
    t += 1
    d = np.sqrt((xb-xf)**2+(yb-yf)**2)

    if(d<100):
        caught = True
        print("Bomber caught at time ",t)
        break
    elif(d>900):
        caught = False
        print("Bomber escaped at time ",t)
        break
    
    xf += v*(xb-xf)/d
    yf += v*(yb-yf)/d

    xb =np.random.randint(0,1000)
    yb = np.random.randint(0,1000)

    fcx.append(xf)
    fcy.append(yf)
    bcx.append(xb)
    bcy.append(yb)

plt.plot(fcx,fcy,'red')
plt.plot(bcx,bcy,'blue')
plt.show()