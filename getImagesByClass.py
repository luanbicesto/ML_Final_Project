import numpy as np
import sys

classFile = '../../code/ML_Final_Project/target/Class11.csv'
classValue = 3
numberClasses = 150

imageClass = np.genfromtxt(classFile, delimiter=',', dtype='int')
images = np.array([imageClass[np.where(imageClass[:, 1] == classValue )]])
images = images[0, :, 0]
firstNImages = images[:numberClasses]
firstNImages = [(str(x) + '.jpg') for x in firstNImages]

print ' '.join(firstNImages)
#[str(x) for x in images[:numberClasses]]
# ",".join([str(x) for x in images[:numberClasses]])

