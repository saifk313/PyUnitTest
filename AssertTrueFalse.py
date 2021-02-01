import unittest
from selenium import webdriver


class AssertTrueFalse(unittest.TestCase):

    def testTrueFalse(self):
        driver = webdriver.Chrome(executable_path="D:/Installers/chromedriver_v88/chromedriver.exe")
        driver.get("https://www.google.com")
        title = driver.title
        self.assertTrue(title == "Google")
        self.assertFalse(title == "Google")
        driver.quit()


if __name__ == "__main__":
    unittest.main()