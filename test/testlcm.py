
x = 11
a = 17
c = 13
m = 100
print("seed :",x)
for i in range(10):

    x = (x*a+c)%m
    print(x)
 