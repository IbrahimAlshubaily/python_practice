from regression import regression
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split

figure, axis = plt.subplots(1, 2, figsize=(14,4))
titles = ['Logistic Regression', 'Linear Regression']
for i, dataset in enumerate([make_classification, make_regression]):
    X, y = dataset(n_samples = 10000, n_features=5)
    X, X_test, y, y_test = train_test_split(X, y)

    clf = regression()
    train_loss, test_loss = clf.fit(train=(X,y), test=(X_test, y_test)) 
    print( 'Test ' + clf.score(X_test, y_test))
    axis[i].plot(range(len(train_loss)), train_loss, label='Train Loss', linewidth=2)
    axis[i].plot(range(len(test_loss)), test_loss, label='Test Loss')
    axis[i].axhline(y=test_loss[-1], color='r', linestyle='--', label=f'Minimum Test Loss ({test_loss[-1]:.2e})')
    axis[i].legend(loc='best')
    axis[i].set_title(titles[i])
figure.savefig('regression_loss_curves.png')
plt.show()
