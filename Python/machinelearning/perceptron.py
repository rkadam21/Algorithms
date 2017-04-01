import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from numpy import random
class Perceptron(object):
    """ Perceptron Classifier.

    Parameters
    -------------
    eta : float
        Learning rate (between 0.0 and 1.0)
    n_iter : int
        Passes over the training dataset.

    Attributes
    -------------
    w_ : 1d-array
        Weights after fitting.
    errors_ : list
        Number of misclassifications in every epoch.

    """
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """Fit training data.

        Parameters
        -------------
        X : {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples
            is the number of samples and
            n_features are the number of features.
        y : array-like, shape = [n_samples]
            Target values.

        Returns
        ---------
        self : object

        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self,X):
        """Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """Return class label afer unit step"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)

ppn = Perceptron(eta=0.1, n_iter=10)
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header= None)
y = df.iloc[0:100, 4].values
y = np.where(y =='Iris-setosa', -1, 1)
X = df.iloc[0:100,[0,2]].values
plt.scatter(X[:50,0], X [:50, 1], color='red', marker = 'o', label = 'setosa')
plt.scatter(X[50:100,0], X [50:100, 1], color='blue', marker = 'x', label = 'versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc = 'upper left')
plt.show()

ppn.fit(X,y)
plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.show()

def plot_decision_boundary(X, y, classifier, resolution=0.02):
    #setup marker generator and color map
    markers = ('s','x','o','^','v')
    colors = ('red','blue','lightgreen','gray','cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    #plot decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 1].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    #plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y == cl, 1], alpha = 0.8
                , c = cmap(idx), marker=markers[idx], label=cl)

plot_decision_boundary(X, y, classifier = ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc = 'upper left')
plt.show()
x = random.randn(5, 5)
print(x)
print(x.T)
mat = x.T.dot(x)
w_ = np.zeros(1 + X.shape[1])
print(X.shape[1])
print(w_)
print(np.dot(X, w_[1:])+ w_[0])
output = np.dot(X, w_[1:])+ w_[0]
error = (y - output)
print(error)
w_[1:] += 0.01 * X.T.dot(error)
print(X.T.dot(error))
print(w_)
w_[0] = 0.01*error.sum()
print(w_)
output = np.dot(X, w_[1:])+ w_[0]
print(output)
error = (y - output)
w_[1:] += 0.01 * X.T.dot(error)
w_[0] = 0.01*error.sum()
print(w_)

output = np.dot(X, w_[1:])+ w_[0]

error = (y - output)
w_[1:] += 0.01 * X.T.dot(error)
w_[0] = 0.01*error.sum()
print(w_)
cost= (error**2).sum() / 2.0
print(cost)
