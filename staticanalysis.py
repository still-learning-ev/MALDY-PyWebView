import pandas as pd
import numpy as np
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

# with open('C:\\Users\\zeeshan lone\\Downloads\\classifier.pkl', 'rb') as f:
#     modl = joblib.load(f)
# with open('C:\\Users\\zeeshan lone\\Downloads\\features.pkl', 'rb') as f:
#     fet = pickle.load(f)

class Analyse:
    def __init__(self):
        with open('classifier.pkl', 'rb') as f:
            self.model = jl.load(f)
        with open('features.pkl', 'rb') as f:
            self.features = pickle.load(f)
        

    def analyse(self,path_to_csv):
        self.data = pd.read_csv(path_to_csv, sep='|')
        #data.head()
        self.heading = list(self.data)
        #print(heading)
        self.to_be_dropped = [x for x in self.heading if x not in self.features]
        self.new_data = self.data.drop(self.to_be_dropped, axis=1)
        self.final_data =self.new_data[0:1]
        self.final_data = np.array(self.final_data)
        self.final_data.reshape(1,-1)
        self.prediction = int(self.model.predict(self.final_data))
        if self.prediction == 0:
            return{'message' : 'The analysed file is potentialy..! Malacious !..'}
        elif self.prediction==1:
            return{'message' : 'The analysed file is potentialy..! Benign !..'}


    def execute_exe(self, path_to_exe):
        os.system('python2 peextractor.py {}'.format(path_to_exe))
        self.result = self.analyse('static_extracted.csv')
        #return {'message':'extraction complete'}
        return self.result


if __name__=='__main__':
    path_to_csv = 'C:\\Users\\zeeshan lone\\Desktop\\datasets\\test-static.csv'
    ana = Analyse()
    ana.analyse(path_to_csv)