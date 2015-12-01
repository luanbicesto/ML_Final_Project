import numpy as np

classFile = '../../code/ML_Final_Project/target/Class11.csv'
classValue = 3
numberClasses = 150

imageClass = np.genfromtxt(classFile, delimiter=',', dtype='int')
images = np.array([imageClass[np.where(imageClass[:, 1] == classValue )]])
images = images[0, :, 0]
firstNImages = images[:(2*numberClasses)]
firstNImages = firstNImages[-numberClasses:]
firstNImagesNew = [(str(x) + '.jpg') for x in firstNImages]

print ' '.join(firstNImagesNew)

# ",".join([str(x) for x in firstNImages])
