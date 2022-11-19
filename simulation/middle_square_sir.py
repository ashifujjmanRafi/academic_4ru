
seed = 675248

def ran():
    global seed
    s = str(seed**2)
    while len(s) != 12:
        s = '0' + s 

    seed = int(s[3:-3])
    return seed

l = []

for i in range(100):
    num = ran()
    l.append(num)
    # print(num, end = ' ')

dup = {x for x in l if l.count(x) > 1}

print(l)
print('\n')
print(dup)
print(len(dup))
