#encoding=utf8

import webbrowser
from wox import Wox,WoxAPI

class Main(Wox):

    def query(self,key):
        
        results = []
        title = key
        url = str(key)
        results.append({"Title": title ,"IcoPath":"Images/app.ico","JsonRPCAction":{"method": "openUrl","parameters":[url],"dontHideAfterAction":True}})

        return results

    def openUrl(self,url):
        chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
        webbrowser.get('chrome').open(url)
        #webbrowser.open()

if __name__ == "__main__":
    Main()
