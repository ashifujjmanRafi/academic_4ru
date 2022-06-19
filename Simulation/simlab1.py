import random
import matplotlib.pyplot as plt
import numpy as np

def pure_pursuit():
    xb = random.randint(0, 1000)
    yb = random.randint(0, 1000)
    xf = random.randint(0, 1000)
    yf = random.randint(0, 1000)

    velocity = 20
    t = 0

    fx = []
    fy = []
    bx = []
    by = []
    fx.append(xf)
    fy.append(yf)
    bx.append(xb)
    by.append(yb)


    caught = False
    while True:
        distance = np.sqrt((xb - xf)**2 + (yb - yf)**2)
        if distance <= 100:
            print("cought")
            caught = True
            break
        elif distance >= 900:
            print("escaped")
            caught = False
            break
        
        sinx = (yb - yf)/distance
        cosx = (xb - xf)/distance
        t = t+1
        xf = xf + velocity*cosx
        yf = yf + velocity*sinx
        fx.append(xf)
        fy.append(yf)

        xb = random.randint(0, 1000)
        yb = random.randint(0, 1000)
        bx.append(xb)
        by.append(yb)

    plt.scatter(fx, fy)
    plt.scatter(bx, by)
    plt.title("Pure Pursuit")
    print("cought/escaped time: ",t )
    plt.show()

pure_pursuit()