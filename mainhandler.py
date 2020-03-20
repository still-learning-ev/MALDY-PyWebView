import threading
import time
import sys
import random
import webview
from statictrain import retrain_model_new
from staticanalysis import Analyse
class Api:
    def __init__(self):
        self.cancel_analysis_flag = False
    
    def start_analysis_static(self, path_to_file, retrain_model):
        time.sleep(1)
        if (str(retrain_model)=='True'):
            retrain_model_new(path_to_file)
        elif(str(retrain_model)=='False'):
            ana = Analyse()
            result = ana.analyse(path_to_file)
        return result


    def start_analysis_exe(self, path_to_exe):
        ana = Analyse()
        result = ana.execute_exe(path_to_exe)
        return result


    def start_analysis_behavioral(self, path_to_file, retrain_model):
        time.sleep(5)
        self.cancel_analysis_flag = False
        for i in range(0, 1000000):
            if self.cancel_analysis_flag:
                response = {'message': 'Analysis cancelled'}
                break
        else:
            response = {
                'message': 'Operation performed on {} and retraining model is {}'.format(path_to_file, retrain_model)
            }
        return response


    def cancel_analysis(self):
        time.sleep(0.1)
        self.cancel_analysis_flag = True

    
