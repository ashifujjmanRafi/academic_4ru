import matplotlib.pyplot as plt

def main():
    t = .1
    k1=.008
    k2=.002
    a=[100]
    b=[50]
    c=[0]

    for i in range(1,60):
        a.append(a[i-1]+(k2*c[i-1]-k1*a[i-1]*b[i-1])*t)
        b.append(b[i-1]+(k2*c[i-1]-k1*a[i-1]*b[i-1])*t)
        c.append (c[i-1]+(2*k1*a[i-1]*b[i-1]-k2*c[i-1])*t)
        print(a[i],b[i],c[i])
    
    plt.plot(a)
    plt.plot(b)
    plt.plot(c)
    plt.legend(['a','b','c'])
    plt.show()
main()