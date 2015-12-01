class=$1
needImageRotation=$2
rotationImages=$3
numberRotations=$4
mode=$5

if [ $mode -eq 1 ]; then
  basedir="trainingImageProcessing/"
else
  basedir="testImageProcessing/"
fi

dirImages="./"$basedir$class"/images"
dirCroppedFull="./"$basedir$class"/cropped/"
dirCropped="./"$basedir$class"/cropped"
dirPercentileFull="./"$basedir$class"/percentile/"
dirPercentile="./"$basedir$class"/percentile"
dirDenoiseTvFull="./"$basedir$class"/denoiseTv/"
dirDenoiseTv="./"$basedir$class"/denoiseTv"
dirHogFull="./"$basedir$class"/hog/"
 
echo "crop and enhance the edges"
rm -rf $basedir$class/cropped/*.*
python selectRegion.py $dirImages $dirCroppedFull # select region of interest and enhance the edges

echo "percentile"
rm -rf $basedir$class/percentile/*.*
python percentile.py $dirCropped $dirPercentileFull # apply filter percentile

echo "denoiseTv"
rm -rf $basedir$class/denoiseTv/*.*
python denoiseTv.py $dirPercentile $dirDenoiseTvFull # remove noisy

if [ $needImageRotation -eq 1 ]; then
  echo "rotate"
  python rotateImage.py $dirDenoiseTvFull $dirDenoiseTvFull $numberRotations $rotationImages
fi

echo "hog"
rm -rf $basedir$class/hog/*.*
python hog.py $dirDenoiseTv $dirHogFull # image descritor

echo "final"
rm -rf $basedir$class/final/*.*
cp $basedir$class/hog/*.* $basedir$class/final
