createAllFoldersClass(){
  classId=$1

  mkdir class_$classId
  cd class_$classId
  mkdir cropped
  mkdir denoiseTv
  mkdir final
  mkdir hog
  mkdir images
  mkdir percentile
  cd ..
}

cd trainingImageProcessing/
createAllFoldersClass 3
createAllFoldersClass 4
createAllFoldersClass 5
createAllFoldersClass 6
createAllFoldersClass 7
createAllFoldersClass 8
createAllFoldersClass 9
createAllFoldersClass 10
createAllFoldersClass 11


