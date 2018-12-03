# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:30:16 2018

@author: Leonardo
"""

"""
The following module will take the Iris dataset and convert it to a usable 
shuffled input matrix for a neural network.

Output training matrix of size:
    rows = features (Sepal Width, Sepal Length, Petal Width, Petal Length)
    columns = size of data set (m)
    
Output label matrix of size:
    rows = label
    columns = size of data set (m)
"""

"""
x1, x2, x3, x4, y = np.genfromtxt('iris.txt', delimiter = ',', unpack=True)
    # assigning labels (see plot data for something more neatly packaged)
    y[0:50] = 0
    y[50:100] = 1
    y[100:150] = 2

"""


# Import packages
# ----------------
import numpy as np
import pandas as pd



# Import data
# ----------------
def convertLabelToSoftmax(labelVector, c):
    # this is analogous to tf.one_hot from tensorflow
    m = labelVector.shape[1]
    y = np.zeros((c, m))
    labelVector = np.ndarray.tolist(labelVector)
    for i in range(m):
        y[int(labelVector[0][i]), i] = 1  # 2nd index to prevent broadcasting
        
    return y


def loadIrisData(filename, testSetSize):
    headers = ['LenSepal', 'WidSepal', 'LenPetal', 'WidPetal', 'Class']
    df = pd.read_csv('iris.txt', names=headers)
    
    LenSepal = df['LenSepal']
    WidSepal = df['WidSepal']
    LenPetal = df['LenPetal']
    WidPetal = df['WidPetal']
    Class = df['Class']
    labels = [0]*len(Class)
    
    for i in range(len(labels)):
        if Class[i] == 'Iris-setosa':
            labels[i] = 0
        elif Class[i] == 'Iris-versicolor':
            labels[i] = 1
        else:
            labels[i] = 2
    
    c = max(labels) + 1
    
    # build feature string as input for np.matrix()
    xStr = ''
    for i in range(len(LenSepal)):    
        xStr += str(LenSepal[i]) + ' '
    xStr += ';'
    for i in range(len(LenSepal)):    
        xStr += str(WidSepal[i]) + ' '
    xStr += ';'
    for i in range(len(LenSepal)):    
        xStr += str(LenPetal[i]) + ' '
    xStr += ';'
    for i in range(len(LenSepal)):    
        xStr += str(WidPetal[i]) + ' '
    
    # shuffle input matrices
    xy = np.matrix(xStr + ';' + str(labels))
    np.random.shuffle(xy.T)
    
    # seperate into train and test sets according to testSetSize
    xTest = xy[0:4, 0:testSetSize]
    yTestTemp = xy[4, 0:testSetSize]
    xTrain = xy[0:4, testSetSize:xy.shape[1]]
    yTrainTemp = xy[4, testSetSize:xy.shape[1]]
    
    # rebuild labels to prepare for softmax
    yTest = convertLabelToSoftmax(yTestTemp, c)
    yTrain = convertLabelToSoftmax(yTrainTemp, c)

    return xTrain, yTrain, xTest, yTest


#testSetSize = 20
#filename = 'iris.txt'

#xTrain, yTrain, xTest, yTest = loadIrisData(filename, testSetSize)



# Initialize Parameters
# ----------------
def initialize(dims):
    # dims is a list stating the number of neurons per layer
    # W and b are dictionaries containing the parameters
    parameters = {}
    
    for i in range(len(dims)):
        if i > 0:
            parameters["W" + str(i)] = np.random.randn(dims[i], dims[i - 1])*0.01
            parameters["b" + str(i)] = np.zeros((dims[i], 1))

    return parameters

#parameters = initialize([4, 3])



# Forward Prop
# ----------------
def forward(A_prev, W, b):
    Z = np.dot(W, A_prev) + b
#    cache = {"A_prev": A_prev, "W": W, "b": b}  # used to compute derivatives
    
    return Z#, cache



# Activation
# ----------------
def activation(Z, activateFcn):
    if activateFcn == 'sigmoid':
        A = 1/(1 + np.exp(-Z))
    elif activateFcn == 'tanh':
        A = 2/(1 + np.exp(-2*Z)) - 1
    elif activateFcn == 'leakyRelu':
        A = max(0.01*Z, Z)
    elif activateFcn == 'unity':
        A = Z
    else:
        # assumed Rectifier Linear Unit (ReLU)
        A = max(0, Z)
        
    return A
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


