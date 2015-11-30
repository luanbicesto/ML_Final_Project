rm -rf testImageProcessing/cropped/*.*
python selectRegion.py './testImageProcessing/images' './testImageProcessing/cropped/' # select region of interest and enhance the edges

rm -rf testImageProcessing/percentile/*.*
python percentile.py './testImageProcessing/cropped' './testImageProcessing/percentile/' # apply filter percentile

rm -rf testImageProcessing/denoiseTv/*.*
python denoiseTv.py './testImageProcessing/percentile' './testImageProcessing/denoiseTv/' # remove noisy

python rotateImage.py

rm -rf testImageProcessing/hog/*.*
python hog.py './testImageProcessing/denoiseTv' './testImageProcessing/hog/' # image descritor

rm -rf testImageProcessing/final/*.*
cp testImageProcessing/hog/*.* testImageProcessing/final
