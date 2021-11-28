from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import numpy as np

def get_obfuscated_dataset():
    digits = datasets.load_digits()
    X = []
    y = digits.target
    for i in range(len(digits.images)):
        X.append(np.concatenate((digits.images[i][0::2,:], digits.images[i][1::2,:])))
        # extract odd rows and even rows and then concatenate them
        X[-1] = np.concatenate((X[-1][:,0::2], X[-1][:,1::2]), axis=1)
        # extract odd columns and even columns and then concatenate them
    return np.array(X), y
    # we need reshape from np, so here convert X into a numpy array.