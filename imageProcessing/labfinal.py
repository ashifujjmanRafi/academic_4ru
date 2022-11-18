import matplotlib.pyplot as plt
import cv2 
import numpy as np

def convulation(img,kernal):
    r,c = img.shape
    x,y = kernal.shape
    out = np.zeros((r-x-1,c-y-1))
    for i in range(r-x-1):
        for j in range(c-y-1):
            x = np.sum(np.multiply(img[i:i+3,j:j+3],kernal))
            if(x<0):
                out[i][j]=0
            elif(x>255):
                out[i][j]=255
            else:
                out[i][j]=x
    return out
def hist(img):
    d = dict()
    for i in range(256):
        d[i]=0
    for i in img:
        for j in i:
            d[j]+= 1
    return d
            


def main():
    img_path = "mountain.jpeg"
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    #assignment3(gray)
    #bitslici_masking(gray)
    #addnoise(gray)



def imginhist():
    img_path = "mountain.jpeg"
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)



    _,binary = cv2.threshold(gray,126,255,cv2.THRESH_BINARY)
    r,c = gray.shape
    binary2 = gray.copy()
    for i in range(r):
        for j in range(c):
            if(gray[i][j]<127):
                binary2[i][j]=0
            else:
                binary2[i][j]=1
    red = rgb[:,:,0]
    green = rgb[:,:,1]
    blue = rgb[:,:,2]

    r = cv2.calcHist([rgb],[0],None,[256],[0,256])
    g = cv2.calcHist([rgb],[1],None,[256],[0,256])
    b = cv2.calcHist([rgb],[2],None,[256],[0,256])
    g = cv2.calcHist([rgb],[0],None,[256],[0,256])
    bi = cv2.calcHist([binary2],[0],None,[256],[0,256])

    hist_list=[r,g,b,g,bi] 
    img_set = [rgb,gray,binary,binary2,red,green,blue]
    imshow(img_set)

def imshow(img_set,x,y):
    for i in range(len(img_set)):
        plt.subplot(x,y,i+1)
        plt.imshow(img_set[i],'gray')
    plt.show()

def assignment2():
    img_path ="mountain.jpeg"
    rgb = plt.imread(img_path)
    img = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    r,c = img.shape
    t1,t2 = 100,140
    #first condition:s = 100, if r >= T1 and r <= T2; otherwise s = 10.
    c1 = img.copy()
    for i in range(r):
        for j in range(c):
            if(img[i][j]>=t1 and img[i][j]<=t2):
                c1[i][j]=100
            else:
                c1[i][j]=10
    #second condition
    c2 = img.copy()
    for i in range(r):
        for j in range(c):
            if(img[i][j]<=t2 and img[i][j]>=t1):
                c2[i][j]= 100
            else:
                c2[i][j]=img[i][j]
    #third condition
    c3 = 3*np.log(img+1)   
    c4 = 3*(1e-6+img) **3 
                
    img_set = [img,c1,c2,c3,c4]
    imshow(img_set,3,2)
    
def assignment3(img):

    hor = np.array([[-2,-2,-2],[0,0,0],[2,2,2]])
    ver = np.array([[2,0,-2],[2,0,-2],[2,0,-2]])
    lapla = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    blur = np.ones((3,3))/9
    edge = np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])

    h = cv2.filter2D(img,-1,hor)
    v = cv2.filter2D(img,-1,ver)
    lap = cv2.filter2D(img,-1,lapla)
    #custom hist custom neighbour processing
    blurim = convulation(img,blur)
    e = convulation(img,edge)

    img_set = [h,v,lap,blurim,e]
    imshow(img_set,2,3)

def bitslici_masking(img):
    r,c = img.shape

    b16 = img&16
    b32 = img&32
    b64 = img&64
    b128 = img&128
    bx = b64+b128+b32
    mask = np.zeros((r,c),dtype=np.uint8)
    mask[40:120,50:250]=255
    mask = mask & img

    img_set=[bx,b16,b32,b64,b128,mask]
    imshow(img_set,3,2)

def addnoise(x):
    img = x.copy()
    r,c = img.shape

    t = r*c//50
    for i in range(t):
        x = np.random.randint(0,r)
        y = np.random.randint(0,c)
        if(i%2==0):
            img[x][y]=255
        else:
            img[x][y]=0
    plt.subplot(1,2,1)
    plt.imshow(img,'gray')
    plt.show()



if __name__=="__main__":
    #imginhist()
    #assignment2()
    main()