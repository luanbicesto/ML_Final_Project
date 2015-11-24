from skimage.feature import hog
from skimage import io, color
import numpy
import os

for filename in os.listdir('./imageProcessing/denoiseTv'):
  image = io.imread('./imageProcessing/denoiseTv/' + filename)
  imageGray = color.rgb2gray(image)

  fd = hog(imageGray, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualise=False)
  numpy.savetxt('./imageProcessing/hog/' + filename[:-24] + ".csv", fd, delimiter=",")
