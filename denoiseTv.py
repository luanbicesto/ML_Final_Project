from skimage import io
from skimage import restoration
import os

for filename in os.listdir('./imageProcessing/percentile'):
  noisy_image = io.imread('./imageProcessing/percentile/' + filename, as_gray=True)
  tv_denoised_image = restoration.denoise_tv_chambolle(noisy_image, weight=0.1)
  io.imsave('./imageProcessing/denoiseTv/' + filename[:-4] + '_tv.jpg', tv_denoised_image)
