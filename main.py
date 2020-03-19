import threading
import time
import sys
import random
import webview
from st import Api
class DefaultApi:
    def got_to_static(self, window):
        time.sleep(10)
        window.load_url('https://pywebview.flowrl.com/hello')
        




if __name__ == '__main__':
    api = Api()
    #api = StaticApi()
  
    window = webview.create_window('MALDY APP','gui/frontpage.html', js_api=api)
    webview.start()
