import pandas as pd
import numpy as np
#from matplotlib import pyplot as plt
import os
import pickle
import sklearn.ensemble as ek
from sklearn.model_selection import cross_validate, train_test_split
from sklearn import tree, linear_model
from sklearn.feature_selection import SelectFromModel
from sklearn.externals import joblib
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn import preprocessing
from sklearn import svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import joblib as jl

def retrain_model_new(path_to_csv):
    malware_data = pd.read_csv(path_to_csv, sep = '|', low_memory = False)
    malware_data_frame = pd.DataFrame(malware_data)

    malware_data_frame[0:1]
    #or malware_data_frame.head()
    malware_data_frame.describe()
    malware_data_frame.groupby(malware_data_frame['legitimate']).size()
    x = malware_data_frame.drop(['Name','md5','legitimate'], axis = 1)
    y = malware_data_frame['legitimate'].values
    print(x[0:3])
    print(y[0:3])
    #extratrees classifier fits a number of ranomised decision trees on various sub samples of the data to imrove predictive.acc
    #this is actually used as parameter here for the feature selection
    #the features contributing the most are selected automatically
    extratrees = ek.ExtraTreesClassifier()
    extratrees.fit(x,y)
    model = SelectFromModel(extratrees, prefit = True)
    x_new = model.transform(x)
    nbfeatures = x_new.shape[1]
    nbfeatures
    #here only 9 features have been selected by the feature selector
    #print(nbfeatures)
    #cross validation is used to divide the dataset into random train test subset
    #it is just like train_test_split() but ranomising the selection of the data in
    X_train, X_test, Y_train, Y_test = train_test_split(x_new, y, test_size = 0.2, shuffle = True, random_state = 42)
    features = []
    index = np.argsort(extratrees.feature_importances_)[::-1][nbfeatures]

    for f in range(nbfeatures):
        #print("%d. features %s (%f)"%(f+1, malware_data_frame.columns[2+index[f]], extratrees.feature_importances_[index[f]]))
        features.append(malware_data_frame.columns[2+f])

    model = {
        "DecisionTree":tree.DecisionTreeClassifier(max_depth = 10),
        "RandomForest":ek.RandomForestClassifier(n_estimators = 50),
        "AdaBoost":ek.AdaBoostClassifier(n_estimators = 50),
        "GradientBoosting":ek.GradientBoostingClassifier(n_estimators = 50),
        "GaussianNB":GaussianNB(),
        "LinearRegression":LinearRegression()
    }

    #training each model with the xtrain and Ytrain then testing with Xtest and Ytest
    results = {}
    for algorithm in model:
        clf = model[algorithm]
        clf.fit(X_train, Y_train)
        score = clf.score(X_test, Y_test)
        print("Algorithm: {}, Score: {}".format(algorithm, score))
        results[algorithm] = score

    we_have_winner = max(results, key=results.get)
    #we_have_winner = 'AdaBoost'
    print(we_have_winner)

    #now we save the model which won among the above models
    #joblib.dump(model[we_have_winner], 'classifier.pkl', compress = 1) for file compressed as only one
    jl.dump(model[we_have_winner], 'classifier.pkl')

    open('features.pkl', 'wb').write(pickle.dumps(features))
    #with open('features.pkl', 'wb') as f:
        #pickle.dump(mylist, f)