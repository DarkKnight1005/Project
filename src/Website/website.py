class Website:
    def __init__(self, siteName, url):
        self.__siteName = siteName
        self.__url = url
    
    def getName(self):
        return self.__siteName

    def getUrl(self):
        return self.__url