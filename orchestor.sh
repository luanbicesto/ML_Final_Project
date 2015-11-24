rm -rf imageProcessing/cropped/*.*
python selectRegion.py # select region of interest and apply enhanceness of edges

rm -rf imageProcessing/percentile/*.*
python percentile.py # apply filter percentile

rm -rf imageProcessing/denoiseTv/*.*
python denoiseTv.py # remove noisy

rm -rf imageProcessing/hog/*.*
python hog.py # image descritor
