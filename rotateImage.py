from PIL import Image
import numpy as np
import sys

fromDir = sys.argv[1]
toDir = sys.argv[2]
numberRotations = sys.argv[3]
imagesToRotate = sys.argv[4]

# fromDir = './trainingImageProcessing/class_1/denoiseTv/'
# toDir = './trainingImageProcessing/class_1/denoiseTv/'
#imagesToRotate = np.array(['126783', '135453', '202788', '209411', '211113', '223904', '227890', '256411', '256893', '284451', '293836', '320852', '345209', '356310', '357133', '373941', '376334', '406866', '437063', '448708', '483706', '496080', '515600', '515861', '516309'])

imagesToRotate = imagesToRotate.split(',')
imagesToRotate = np.array(imagesToRotate)
imageSufix = '_cropped_edge_per_tv.jpg'
expandValue = 1
prefixRotatedImage = '99999'
size = 175, 175
numberRotations = int(numberRotations)
offSetAngle = 359 / numberRotations

for i in range(imagesToRotate.size):
  interaction = 1
  imageName = str(imagesToRotate[i])
  imageFullName = imageName + imageSufix
  srcImage = Image.open(fromDir + imageFullName)

  while (interaction <= numberRotations):
    rotatedImage = srcImage.rotate(offSetAngle * interaction, expand=1)
    rotatedImage.thumbnail(size, Image.ANTIALIAS)
    rotatedImage.save(toDir + prefixRotatedImage + str(interaction) + imageFullName)
    interaction = interaction + 1
