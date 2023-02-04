import matplotlib.pyplot as plt
import cv2
import numpy as np



def assignment1():
    img_path = "mountain.jpeg"
    rgb = plt.imread(img_path)
    print(rgb.shape)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    print(gray.shape)
    binary = np.zeros((gray.shape), dtype=np.uint8)
    r, c = gray.shape
    # for i in range(r):
    #     for j in range(c):
    #         if(gray[i][j]<127):
    #             binary[i][j]=0
    #         else:
    #             binary[i][j]=255
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    red = rgb[:, :, 0]
    green = rgb[:, :, 1]
    blue = rgb[:, :, 2]

    # histogram
    r1 = cv2.calcHist([rgb], [0], None, [256], [0, 256])
    g1 = cv2.calcHist([rgb], [1], None, [256], [0, 256])
    b1 = cv2.calcHist([rgb], [2], None, [256], [0, 256])
    gray1 = cv2.calcHist([gray], [0], None, [256], [0, 256])
    binary1 = cv2.calcHist([binary], [0], None, [256], [0, 256])

    img_set = [red, green, blue, gray, binary]
    plot_set = [r1, g1, b1, gray1, binary1]

    # print
    for i in range(len(img_set)):
        plt.subplot(2, 5, i+1)
        plt.imshow(img_set[i], 'gray')
        plt.subplot(2, 5, i+6)
        plt.plot(plot_set[i])
    plt.tight_layout()
    plt.show()


def assingment2(gray):

    print(gray.shape)
    r, c = gray.shape
    print(c)
    t1, t2 = 50, 120
    epsilon = 1e-6
    co, p = 3, 2

    out1 = np.zeros((r, c), dtype=np.uint8)
    print(out1.shape)
    for i in range(r):
        for j in range(c):
            if(gray[i][j] >= t1 and gray[i][j] <= t2):
                out1[i][j] = 100
            else:
                out1[i][j] = 10

    out2 = np.zeros((r, c), dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            if(gray[i][j] >= t1 and gray[i][j] <= t2):
                out2[i][j] = 100
            else:
                out2[i][j] = gray[i][j]

    out3 = co * ((epsilon+gray)**p)
    out4 = co * np.log(1+gray)

    img_set = [out1, out2, out3, out4]
    for i in range(len(img_set)):
        plt.subplot(2, 2, i+1)
        plt.imshow(img_set[i], 'gray')

    plt.show()


def assignment3(gray):
    hor_kernal = np.array([[2, 10, 2], [0, 0, 0], [-2, -10, -2]])
    ver_kernal = np.array([[-2, 0, 2], [-10, 0, 10], [-2, 0, 2]])
    box_kernal = np.ones((3, 3))/9
    sharpn_kernal = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    out1 = cv2.filter2D(gray, -1, hor_kernal)
    out2 = cv2.filter2D(gray, -1, ver_kernal)
    out3 = cv2.filter2D(gray, -1, box_kernal)
    out4 = cv2.filter2D(gray, -1, sharpn_kernal)

    img_set = [out1, out2, out3, out4]
    for i in range(len(img_set)):
        plt.subplot(2, 2, i+1)
        plt.imshow(img_set[i], 'gray')
    plt.show()


def assignment4(rgb, gray):
    # custom histogram:
    d = dict()
    for i in range(256):
        d[i] = 0
    for i in rgb[:, :, 0]:
        for j in i:
            d[j] += 1

    red = cv2.calcHist([rgb], [0], None, [256], [0, 256])
    plot_set = [d, red]

    plt.subplot(2, 2, 1)
    plt.title("custom")
    plt.plot(d.keys(), d.values())

    plt.subplot(2, 2, 2)
    plt.title("builtin")
    plt.plot(red)

    # custom convulation:
    kernal = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    r, c = gray.shape
    x, y = kernal.shape
    out = np.zeros((r-x-1, c-y-1))
    for i in range(r-x-1):
        for j in range(c-y-1):
            sum = np.sum(np.multiply(gray[i:i+x, j:j+y], kernal))
            if(sum < 0):
                out[i][j] = 0
            elif(sum > 255):
                out[i][j] = 255
            else:
                out[i][j] = sum
    # builtin convulation
    out1 = cv2.filter2D(gray, -1, kernal)
    img_set = [out, out1]
    for i in range(len(img_set)):
        plt.subplot(2, 2, i+3)
        plt.imshow(img_set[i], 'gray')
    plt.show()


def assingment5(gray):
    bit1, bit2, bit3, bit4 = gray.copy(), gray.copy(), gray.copy(), gray.copy()
    bit1 = gray & 16
    bit2 = gray & 32
    bit3 = gray & 64
    bit4 = gray & 128
    bit5 = bit1+bit2+bit3+bit4
    print(bit5.shape)

    # masking
    mask = np.zeros((gray.shape), dtype=np.uint8)
    mask[50:120, 80:150] = 255
    mask = mask & gray
    img_set = [bit1, bit2, bit3, bit4, bit5, mask]
    for i in range(len(img_set)):
        plt.subplot(2, 3, i+1)
        plt.imshow(img_set[i], 'gray')
    plt.show()


def assignment6(gray):
    salt = gray.copy()
    kernal = np.ones((3, 3), dtype=np.uint8)/9
    r, c = salt.shape

    t = r*c // 50
    for i in range(t):
        x = np.random.randint(0, r)
        y = np.random.randint(0, c)
        if(i % 2 == 0):
            salt[x][y] = 255
        else:
            salt[x][y] = 0
    filtered = cv2.filter2D(salt, -1, kernal)
    img_set = [salt, filtered]
    for i in range(len(img_set)):
        plt.subplot(2, 1, i+1)
        plt.imshow(img_set[i], 'gray')
    plt.show()


def assignment7_10(gray):
    r, c = gray.shape
    left, right, narrow, equlize = gray.copy(), gray.copy(), gray.copy(), gray.copy()

    left = gray - 80
    right = gray + 50
    for i in range(r):
        for j in range(c):
            if(narrow[i][j] < 100):
                narrow[i][j] = 100
            elif(narrow[i][j] > 180):
                narrow[i][j] = 180
    equlize = cv2.equalizeHist(gray)
    l = cv2.calcHist([left], [0], None, [256], [0, 256])
    r = cv2.calcHist([right], [0], None, [256], [0, 256])
    n = cv2.calcHist([narrow], [0], None, [256], [0, 256])
    eq = cv2.calcHist([equlize], [0], None, [256], [0, 256])

    plot_set = [l, r, n, eq]
    for i in range(len(plot_set)):
        plt.subplot(2, 2, i+1)
        plt.plot(plot_set[i])
    plt.show()

def assignment8(binary):
    kernal = np.ones((5, 5), dtype=np.uint8)

    ero = cv2.erode(binary, kernal)
    dil = cv2.dilate(binary, kernal)

    opening = cv2.erode(dil, kernal)
    closing = cv2.dilate(ero, kernal)
    img_set = [ero, dil, opening, closing]

    for i in range(len(img_set)):
        plt.subplot(2,2,i+1)
        plt.imshow(img_set[i],'gray')
    plt.show() 

def main():

    img_path = "mountain.jpeg"
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    # assignment1()
    # assingment2(gray)
    # assignment3(gray)
    # assignment4(rgb,gray)
    # assingment5(gray)
    # assignment6(gray)
    # assignment7_10(gray)

    _, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    #assignment8(binary)  
    
    



    

   



    

    

    

    
    

if __name__=="__main__":
    main()