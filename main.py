import threading
import time
import sys
import random
import webview
from mainhandler import Api




if __name__ == '__main__':
    api = Api()
    
  
    window = webview.create_window('MALDY APP','gui/frontpage.html', js_api=api)
    webview.start()
