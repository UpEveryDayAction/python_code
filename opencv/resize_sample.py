import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Lenna.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image = cv2.resize(image, None, fx=0.1, fy=0.1,
                   interpolation=cv2.INTER_NEAREST)

h, w = image.shape[:2]

plt.subplot(2, 3, 1)
plt.title('original')
plt.imshow(image)

plt.subplot(2, 3, 2)
resized_image = cv2.resize(image, (w * 2, h * 2),
                           interpolation=cv2.INTER_NEAREST)
plt.title('cv2.INTER_NEAREST')
plt.imshow(resized_image)

plt.subplot(2, 3, 3)
resized_image = cv2.resize(image, (w * 2, h * 2),
                           interpolation=cv2.INTER_LINEAR)
plt.title('cv2.INTER_LINEAR')
plt.imshow(resized_image)

plt.subplot(2, 3, 4)
resized_image = cv2.resize(image, (w * 2, h * 2),
                           interpolation=cv2.INTER_AREA)
plt.title('cv2.INTER_AREA')
plt.imshow(resized_image)

plt.subplot(2, 3, 5)
resized_image = cv2.resize(image, (w * 2, h * 2),
                           interpolation=cv2.INTER_CUBIC)
plt.title('cv2.INTER_CUBIC')
plt.imshow(resized_image)

plt.subplot(2, 3, 6)
resized_image = cv2.resize(image, (w * 2, h * 2),
                           interpolation=cv2.INTER_LANCZOS4)
plt.title('cv2.INTER_LANCZOS4')
plt.imshow(resized_image)

plt.show()