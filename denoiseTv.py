from skimage import io
from skimage import restoration
import os
import sys

fromDir = sys.argv[1] # .../percentile
toDir = sys.argv[2] # .../denoiseTv/

for filename in os.listdir(fromDir):
  noisy_image = io.imread(fromDir + '/' + filename, as_gray=True)
  tv_denoised_image = restoration.denoise_tv_chambolle(noisy_image, weight=0.1)
  io.imsave(toDir + filename[:-4] + '_tv.jpg', tv_denoised_image)
