import numpy as np
import matplotlib.pyplot as plt
import cv2

# Define the DCT and IDCT functions
def dct(x):
    return np.fft.fft2(x, norm='ortho')

def idct(x):
    return np.real(np.fft.ifft2(x, norm='ortho'))

# Load the image
img = plt.imread('image.jpg')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Apply DCT on the grayscale image
dct_img = dct(gray_img)

# Plot the DCT transformed image
plt.imshow(np.abs(dct_img), cmap='gray')
plt.title('DCT Transformed Image')
plt.show()

# Apply IDCT on the transformed image
idct_img = idct(dct_img)

# Plot the reconstructed image
plt.imshow(idct_img, cmap='gray')
plt.title('Reconstructed Image')
plt.show()
