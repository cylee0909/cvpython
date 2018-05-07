#encoding:utf-8
#傅立叶变换
import cv2
import numpy as np
from matplotlib import pyplot as plt

#傅立叶变换将图像从空间域变换到频率域

#性能问题，如果图像的尺寸是2 、3、5的级数则计算效率会比较高，使用cv2.getOptimalDFTSize()可以获取优化size


# #fft in numpy
# img = cv2.imread('dog.jpg',0) #get the gray image
# f = np.fft.fft2(img) # fft 变换
# # fshift=f
# fshift = np.fft.fftshift(f) # shift the result. befor shift dc component is at top left corner
# magnitude_spectrum = 20*np.log(np.abs(fshift))

# rows, cols = img.shape
# crow,ccol = rows/2 , cols/2
# fshift[crow-30:crow+30, ccol-30:ccol+30] = 0 #low frequency be removed like High Pass Filtering
# f_ishift = np.fft.ifftshift(fshift) # inverse the shift
# img_back = np.fft.ifft2(f_ishift) # inverse the fft
# img_back = np.abs(img_back) #get image back

# plt.subplot(131),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
# plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])

# plt.show()

#fft in opencv which is faster than numpy
img = cv2.imread('dog.jpg',0)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft) #此函数返回实部和虚部两个数组组成的数组
print len(dft_shift), len(dft_shift[0]), len(dft_shift[0][0])
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])) #计算幅值 也可通过cv2.cartToPolar()函数来计算幅值和幅角

rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-60:crow+60, ccol-60:ccol+60] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask #高频为零，类似低通滤波
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
plt.title('Back Image'), plt.xticks([]), plt.yticks([])
plt.show()