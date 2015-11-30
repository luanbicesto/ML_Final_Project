from PIL import Image
import numpy as np

fromDir = './trainingImageProcessing/denoiseTv/'
toDir = './trainingImageProcessing/denoiseTv/'
imagesToRotate = np.array(['126783', '135453', '202788', '209411', '211113', '223904', '227890', '256411', '256893', '284451', '293836', '320852', '345209', '356310', '357133', '373941', '376334', '406866', '437063', '448708', '483706', '496080', '515600', '515861', '516309'])

imageSufix = '_cropped_edge_per_tv.jpg'
numberRotations = 16
expandValue = 1
prefixRotatedImage = '99999'
size = 175, 175
offSetAngle = 359 / numberRotations

for i in range(imagesToRotate.size):
  interaction = 1
  imageName = imagesToRotate[i]
  imageFullName = imageName + imageSufix
  srcImage = Image.open(fromDir + imageFullName)

  while (interaction <= numberRotations):
    rotatedImage = srcImage.rotate(offSetAngle * interaction, expand=1)
    rotatedImage.thumbnail(size, Image.ANTIALIAS)
    rotatedImage.save(toDir + prefixRotatedImage + str(interaction) + imageFullName)
    interaction = interaction + 1
