def lcm(x0, a, c, m, r_num, n):
    r_num[0] = x0
    for i in range(1, n):
        r_num[i] = ((r_num[i-1] * a) + c) % m

def main():
    x0 = 1
    a = 1103515245
    c = 4312345
    m = 2**32
    n = 50000
    r_num = [0] * n

    lcm (x0, a, c, m, r_num, n)

    for i in range(n):
        print(r_num[i], end = ' ')

    dup = {x for x in r_num if r_num.count(x) > 1}

    print('\n')
    print(dup)
    print(len(dup))

if __name__ == '__main__':
    main()
