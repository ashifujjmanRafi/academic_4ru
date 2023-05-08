import numpy as np
import matplotlib.pyplot as plt

# Create a 16x16 gray level image with random values
image = np.random.rand(16, 16) * 255

# Apply DCT on the image
dct_image = np.round(np.fft.dct(np.fft.dct(image.T, norm='ortho').T, norm='ortho'))

# Plot the DCT transformed image
plt.imshow(dct_image, cmap='gray')
plt.title('DCT Transformed Image')
plt.show()

# Apply IDCT on the transformed image
idct_image = np.round(np.fft.idct(np.fft.idct(dct_image.T, norm='ortho').T, norm='ortho'))

# Plot the IDCT transformed image
plt.imshow(idct_image, cmap='gray')
plt.title('IDCT Transformed Image')
plt.show()
