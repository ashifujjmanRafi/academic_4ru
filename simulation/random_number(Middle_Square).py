num_x = []

def main():
    x = 14
    n = 10

    num_x.append(x)

    for i in range(n):
        num_new = random_number()
        print(num_new)

def random_number():
    num = num_x[-1] ** 2
    num_str = str(num).zfill(4)

    middle = int(num_str[1:3])
    num_x.append(middle)

    return middle    

if __name__ == "__main__":
    main()