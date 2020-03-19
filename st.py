import threading
import time
import sys
import random
import webview

class Api:
    def __init__(self):
        self.cancel_analysis_flag = False
    
    def start_analysis_static(self, path_to_file, retrain_model):
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

    
