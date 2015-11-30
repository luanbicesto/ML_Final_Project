
rm -rf trainingImageProcessing/cropped/*.*
python selectRegion.py './trainingImageProcessing/images' './trainingImageProcessing/cropped/' # select region of interest and enhance the edges

rm -rf trainingImageProcessing/percentile/*.*
python percentile.py './trainingImageProcessing/cropped' './trainingImageProcessing/percentile/' # apply filter percentile

rm -rf trainingImageProcessing/denoiseTv/*.*
python denoiseTv.py './trainingImageProcessing/percentile' './trainingImageProcessing/denoiseTv/' # remove noisy

python rotateImage.py

rm -rf trainingImageProcessing/hog/*.*
python hog.py './trainingImageProcessing/denoiseTv' './trainingImageProcessing/hog/' # image descritor

rm -rf trainingImageProcessing/final/*.*
cp trainingImageProcessing/hog/*.* trainingImageProcessing/final
