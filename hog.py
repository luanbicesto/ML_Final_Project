from skimage.feature import hog
from skimage import io, color
import numpy
import os
import sys

fromDir = sys.argv[1] # .../denoiseTv
toDir = sys.argv[2] # .../hog/

for filename in os.listdir(fromDir):
  image = io.imread(fromDir + '/' + filename)
  imageGray = color.rgb2gray(image)

  fd = hog(imageGray, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualise=False)
  numpy.savetxt(toDir + filename[:-24] + ".csv", fd, delimiter=",")
