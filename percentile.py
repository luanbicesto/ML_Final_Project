import scipy
from scipy import ndimage
import os
import sys

fromDir = sys.argv[1] # .../cropped
toDir = sys.argv[2] # .../percentile/

for filename in os.listdir(fromDir):
  image = scipy.misc.imread(fromDir + "/" + filename)
  im_med = ndimage.percentile_filter(image, 1, 2)
  scipy.misc.imsave(toDir + filename[:-4] + "_per.jpg", im_med)
