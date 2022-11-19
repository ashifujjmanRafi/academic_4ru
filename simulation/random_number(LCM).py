num_x = []

def main():
    x = 27
    a = 17
    c = 43
    m = 100
    n = 10

    num_x.append(x)
    
    for i in range(n):
        num_new = random_Number(a, c, m)
        print(num_new)
    
    # print(num_x)

def random_Number(a, c, m):
    x_temp = (a * num_x[-1] + c) % m
    num_x.append(x_temp)
    return x_temp

if __name__ == "__main__":
    main()
