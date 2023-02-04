import cv2

def jpg2png():
    img_path = "chan.jpg"

    name,format = img_path.split(".")

    if format == 'jpeg' or format == 'jpg':
        img = cv2.imread(img_path)
        cv2.imwrite(name+".png", img)
    else:
        img = cv2.imread(img_path)
        cv2.imwrite(name+".jpeg", img)

if __name__ == "__main__":
    jpg2png()