# rm -rf trainingImageProcessing/images/*.*
# rm -rf testImageProcessing/images/*.*

cd ../../data/training_part
cp `python ../../code/ML_Final_Project/getImagesByClass.py` ../../code/ML_Final_Project/trainingImageProcessing/class_11/images
cd ../../code/ML_Final_Project

cd ../../data/training_part
cp `python ../../code/ML_Final_Project/getTestImagesByClass.py` ../../code/ML_Final_Project/testImageProcessing/class_11/images
cd ../../code/ML_Final_Project
