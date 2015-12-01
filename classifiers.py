from __future__ import division
import os
import csv
import numpy as np
import math
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

trainingBaseDir = './trainingImageProcessing/'
testBaseDir = './testImageProcessing/'
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
  training = training + 'class_1/final/'
  test = test + 'class_1/final/'

  classifierRandomForests(training, test, 'train_test', 3, './confusionMatrix/class_1/', 240, 'Class1.csv')
  classifierRandomForests(test, training, 'test_train', 3, './confusionMatrix/class_1/', 240, 'Class1.csv')
  # classifierClass1Detail(training, test, 'train_test')
  # classifierClass1Detail(test, training, 'test_train')

def classifierClass2(training, test):
  training = training + 'class_2/final/'
  test = test + 'class_2/final/'

  classifierLogR(training, test, 'train_test', './confusionMatrix/class_2/', 'Class2.csv')
  classifierLogR(test, training, 'test_train', './confusionMatrix/class_2/', 'Class2.csv')

def buildLogRClassifier(normalizedInputData, expectedValues):
  clf = LogisticRegression()
  clf = clf.fit(normalizedInputData, expectedValues[:, 0, 1])
  return clf

def classifierLogR(trainingDir, testDir, name, baseDirConfusionMatrix, targetValuesClass):
  normalizedInputData, expectedValues, columnMean, columnSd, targetClass = getTrainingData(trainingDir, baseDirConfusionMatrix, targetBaseDir + targetValuesClass)

  clf = buildLogRClassifier(normalizedInputData, expectedValues)

  applyTest(testDir, clf, columnMean, columnSd, targetClass, 2, baseDirConfusionMatrix, name)

def getTrainingData(trainingDir, baseDir, targetDir): #confusionMatrixDir
  sortedInputData, galaxyIds = buildInputMatrix(trainingDir)
  normalizedInputData, columnMean, columnSd = normalizeInputData(sortedInputData)
  
  np.savetxt(baseDir + 'mean.csv', columnMean, delimiter=",")
  np.savetxt(baseDir + 'sd.csv', columnSd, delimiter=",")

  targetClass = np.genfromtxt(targetDir, delimiter=',', dtype='int')
  targetClassSpecific = np.array([targetClass[np.where(targetClass[:, 0] == int(x))] for x in galaxyIds])

  return (normalizedInputData, targetClassSpecific, columnMean, columnSd, targetClass)

def buildRandomForestClassifier(numberTrees, normalizedInputData, expectedValues):
  clf = RandomForestClassifier(n_estimators = numberTrees)
  clf = clf.fit(normalizedInputData, expectedValues[:, 0, 1])
  return clf

def applyTest(testDir, clf, columnMean, columnSd, targetClass, numberClasses, baseDirConfusionMatrix, name):
  testSortedInputData, testGalaxyIds = buildInputMatrix(testDir)
  rows, cols = testSortedInputData.shape

  testNormalizedInputData = normalizeTestInputData(testSortedInputData, columnMean, columnSd, cols)
  testTargetClassSpecific = np.array([targetClass[np.where(targetClass[:, 0] == int(x))] for x in testGalaxyIds])

  confusionMatrix = buildConfusionMatrix(clf, testNormalizedInputData, testTargetClassSpecific, numberClasses)
  print(confusionMatrix)
  np.savetxt(baseDirConfusionMatrix + name + ".csv", confusionMatrix, delimiter=",")
  return

def classifierRandomForests(trainingDir, testDir, name, numberClasses, baseDirConfusionMatrix, numberTrees, targetValuesClass):
  # baseDirConfusionMatrix = './confusionMatrix/class_1/'
  # numberTrees = 240

  # sortedInputData, galaxyIds = buildInputMatrix(trainingDir)
  # normalizedInputData, columnMean, columnSd = normalizeInputData(sortedInputData)
  # np.savetxt(baseDirConfusionMatrix + 'mean.csv', columnMean, delimiter=",")
  # np.savetxt(baseDirConfusionMatrix + 'sd.csv', columnSd, delimiter=",")
  # targetClass1 = np.genfromtxt(targetBaseDir + 'Class1.csv', delimiter=',', dtype='int')
  # targetClassSpecific = np.array([targetClass1[np.where(targetClass1[:, 0] == int(x))] for x in galaxyIds])
  normalizedInputData, expectedValues, columnMean, columnSd, targetClass = getTrainingData(trainingDir, baseDirConfusionMatrix, targetBaseDir + targetValuesClass)

  # build forest 
  # clf = RandomForestClassifier(n_estimators = numberTrees)
  # clf = clf.fit(sortedInputData, targetClassSpecific[:, 0, 1])
  clf = buildRandomForestClassifier(numberTrees, normalizedInputData, expectedValues)

  # test
  # testSortedInputData, testGalaxyIds = buildInputMatrix(testDir)
  # rows, cols = testSortedInputData.shape

  # testNormalizedInputData = normalizeTestInputData(testSortedInputData, columnMean, columnSd, cols)
  # testTargetClassSpecific = np.array([targetClass1[np.where(targetClass1[:, 0] == int(x))] for x in testGalaxyIds])

  # confusionMatrix = buildConfusionMatrix(clf, testNormalizedInputData, testTargetClassSpecific, 3)
  # print(confusionMatrix)
  # np.savetxt(baseDirConfusionMatrix + name + ".csv", confusionMatrix, delimiter=",")

  applyTest(testDir, clf, columnMean, columnSd, targetClass, numberClasses, baseDirConfusionMatrix, name)

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
classifierClass1(trainingBaseDir, testBaseDir)

# classifier class 2
classifierClass2(trainingBaseDir, testBaseDir)

