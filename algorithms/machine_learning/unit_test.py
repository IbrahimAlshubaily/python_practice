from linear_regression import linear_regression
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

X, y = make_regression(n_features=5)
X, X_test, y, y_test = train_test_split(X, y)

clf = linear_regression()
train_loss, test_loss = clf.fit(train=(X,y), test=(X_test, y_test)) 
figure, axis = plt.subplots(1, 2, figsize=(14,4))
axis[0].scatter(range(len(X_test)), y_test, label='Ground Truth')
axis[0].plot(range(len(X_test)), clf.predict(X_test), 'r', label='Prediction')

axis[1].plot(range(len(train_loss)), train_loss, label='Train Loss')
axis[1].plot(range(len(test_loss)), test_loss, label='Test Loss')
axis[0].legend(loc='upper right')
axis[1].legend(loc='upper right')
figure.savefig('./linear_regression_result.png')