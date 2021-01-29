import unittest
from selenium import webdriver


class SearchEngineTest(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="D:/Installers/chromedriver_v88/chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title:", self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="D:/Installers/chromedriver_v88/chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Title:", self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
