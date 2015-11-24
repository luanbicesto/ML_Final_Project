from PIL import Image
import ImageFilter
import os

for filename in os.listdir('./imageProcessing/images'):
  im = Image.open("./imageProcessing/images/" + filename)

  crop_rectangle = (125, 125, 300, 300)
  cropped_im = im.crop(crop_rectangle)

  # Filter Edge
  im_edge = cropped_im.filter(ImageFilter.EDGE_ENHANCE_MORE)
  im_edge.save("./imageProcessing/cropped/" + filename[:-4] + "_cropped_edge.jpg")

  # to be deleted
  # cropped_im.show()
  # cropped_im.save('100474_per_after.jpg')

