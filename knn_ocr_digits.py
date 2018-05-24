#encoding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('digits.png') #1000hx2000w
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print gray.shape
# Now we split the image to 5000 cells, each 20x20 size
cells=[np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
print type(cells)
# Make it into a Numpy array. It size will be (50,100,20,20)
x = np.array(cells)
print type(x), len(x), len(x[0])
# Now we prepare train_data and test_data.
train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)

# Create labels for train and test data
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]
test_labels = train_labels.copy()

# Initiate kNN, train the data, then test it with test data for k=1
knn = cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE, train_labels)
ret,result,neighbours,dist = knn.findNearest(test,k=5)

# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result==test_labels
print test_labels[matches == 0] ,'\n', result[matches == 0]
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print accuracy

## save the data
# np.savez('knn_data.npz',train=train, train_labels=train_labels)

# 对于训练数据，我们可以直接存储在文件中，下次识别的时候直接读取分类数据进行分类即可
# Now load the data
# with np.load('knn_data.npz') as data:
#     print data.files
#     train = data['train']
#     train_labels = data['train_labels']