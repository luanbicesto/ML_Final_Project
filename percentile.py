import scipy
from scipy import ndimage
import os

for filename in os.listdir('./imageProcessing/cropped'):
  image = scipy.misc.imread("./imageProcessing/cropped/" + filename)
  im_med = ndimage.percentile_filter(image, 1, 2)
  scipy.misc.imsave("./imageProcessing/percentile/" + filename[:-4] + "_per.jpg", im_med)
