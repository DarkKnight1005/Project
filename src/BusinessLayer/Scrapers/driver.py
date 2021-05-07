from selenium import webdriver

class Driver:
    def __init__(self, browser, name):
        self.name = name;
        self.__browser = webdriver.Chrome(executable_path=browser)

    def getBrowser(self):
        return self.__browser
    
    def setBrowser(self, newBrowser):
        self.__browser = webdriver.Chrome(executable_path=newBrowser)
        return self.__browser
