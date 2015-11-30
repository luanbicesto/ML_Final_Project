from __future__ import division
import os
import csv
import numpy as np
import math
from sklearn.ensemble import RandomForestClassifier

trainingDir = './trainingImageProcessing/final/'
testDir = './testImageProcessing/final/'
targetBaseDir = './target/'
idGalaxySize = 6

def buildInputMatrix(fromDir):
  first = 0
  for filename in os.listdir(fromDir):
    descImage = np.genfromtxt(fromDir + filename, delimiter=',', dtype='float')
    descImage = np.hstack((descImage, (float(filename[:-4]) % math.pow(10, idGalaxySize)) ))
    
    if first == 0:
      inputMatrix = np.array(descImage)
      first = 1
    else:
      # print(descImage.shape)
      inputMatrix = np.vstack((inputMatrix, descImage))
  # sort by the last column
  rows, cols = inputMatrix.shape
  sortedInputData = np.array(sorted(inputMatrix, key=lambda x:x[cols-1]))
  galaxyIds = sortedInputData[:, cols-1]
  sortedInputData = np.delete(sortedInputData, cols-1, 1)
  return (sortedInputData, galaxyIds)

def classifierClass1(training, test):
  classifierClass1Detail(training, test, 'train_test')
  classifierClass1Detail(test, training, 'test_train')

def classifierClass1Detail(trainingDir, testDir, name):
  baseDirConfusionMatrix = './confusionMatrix/class_1/'
  numberTrees = 240

  sortedInputData, galaxyIds = buildInputMatrix(trainingDir)
  normalizedInputData, columnMean, columnSd = normalizeInputData(sortedInputData)

  targetClass1 = np.genfromtxt(targetBaseDir + 'Class1.csv', delimiter=',', dtype='int')
  targetClassSpecific = np.array([targetClass1[np.where(targetClass1[:, 0] == int(x))] for x in galaxyIds])

  # build forest 
  clf = RandomForestClassifier(n_estimators = numberTrees)
  clf = clf.fit(sortedInputData, targetClassSpecific[:, 0, 1])

  # test
  testSortedInputData, testGalaxyIds = buildInputMatrix(testDir)
  rows, cols = testSortedInputData.shape

  testNormalizedInputData = normalizeTestInputData(testSortedInputData, columnMean, columnSd, cols)
  testTargetClassSpecific = np.array([targetClass1[np.where(targetClass1[:, 0] == int(x))] for x in testGalaxyIds])

  confusionMatrix = buildConfusionMatrix(clf, testNormalizedInputData, testTargetClassSpecific, 3)
  print(confusionMatrix)
  np.savetxt(baseDirConfusionMatrix + name + ".csv", confusionMatrix, delimiter=",")

def normalizeTestInputData(inputData, columnMean, columnSd, cols):
  normalizedTestInputData = [[(x - columnMean[j]) / columnSd[j] for x in inputData[:, j]] for j in range(cols)]
  return np.array(normalizedTestInputData).T

def normalizeInputData(inputData):
  # z-norm
  baseDirZnorm = './normalization/'
  rows, cols = inputData.shape
  columnMean = np.mean(inputData, axis = 0)
  columnSd = np.std(inputData, axis = 0)
  normalizedInputData = [[(x - columnMean[j]) / columnSd[j] for x in inputData[:, j]] for j in range(cols)]
  normalizedInputData = np.array(normalizedInputData)
  normalizedInputData = normalizedInputData.T

  np.savetxt(baseDirZnorm + 'mean.csv', columnMean, delimiter=",")
  np.savetxt(baseDirZnorm + 'sd.csv', columnSd, delimiter=",")

  return (normalizedInputData, columnMean, columnSd) 

def buildConfusionMatrix(classifier, testData, expectedValues, numberOfClasses):
  confusionMatrix = [[0 for x in range(numberOfClasses)] for x in range(numberOfClasses)]
  predictedValues = classifier.predict(testData)

  for i in range(0, len(predictedValues)):
    confusionMatrix[expectedValues[i][0][1] - 1][predictedValues[i] - 1]+=1

  sumOfClass = np.sum(confusionMatrix, axis=1)
  sumOfClass[sumOfClass == 0] = 1
  confusionMatrix = np.array(confusionMatrix)
  # print(confusionMatrix)
  confusionMatrix = [[x / sumOfClass[i] for x in confusionMatrix[i, :]] for i in range(sumOfClass.size)]
  
  return (confusionMatrix)

# classifier class 1
classifierClass1(trainingDir, testDir)

