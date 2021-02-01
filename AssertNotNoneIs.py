import unittest
from selenium import webdriver


class AssertNotNoneIs(unittest.TestCase):

    def testIsNotNone(self):
        driver = webdriver.Chrome(executable_path="D:/Installers/chromedriver_v88/chromedriver.exe")
        driver.get("https://www.google.com/")
        title = driver.title
        self.assertIsNone(title, "Title is google")
        self.assertIsNotNone(title, "Title is not none")
        driver.quit()


if __name__ == "__main__":
    unittest.main()
