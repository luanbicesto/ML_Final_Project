# rm -rf trainingImageProcessing/images/*.*
# rm -rf testImageProcessing/images/*.*

# class 1
cd ../../data/images_training_rev1
cp `python ../../code/ML_Final_Project/getImagesByClass.py` ../../code/ML_Final_Project/trainingImageProcessing/images
cd ../../code/ML_Final_Project

cd ../../data/images_training_rev1
cp `python ../../code/ML_Final_Project/getTestImagesByClass.py` ../../code/ML_Final_Project/testImageProcessing/images
cd ../../code/ML_Final_Project
