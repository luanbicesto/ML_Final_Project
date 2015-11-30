from PIL import Image
import ImageFilter
import os
import sys

fromDir = sys.argv[1] # .../images
toDir = sys.argv[2] # .../cropped/

for filename in os.listdir(fromDir):
  im = Image.open(fromDir + "/" + filename)

  crop_rectangle = (125, 125, 300, 300)
  cropped_im = im.crop(crop_rectangle)

  # Filter Edge
  im_edge = cropped_im.filter(ImageFilter.EDGE_ENHANCE_MORE)
  im_edge.save(toDir + filename[:-4] + "_cropped_edge.jpg")

  # to be deleted
  # cropped_im.show()
  # cropped_im.save('100474_per_after.jpg')

