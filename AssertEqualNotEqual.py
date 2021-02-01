import unittest
from selenium import webdriver


class AssertEqNotEq(unittest.TestCase):

    def testTitle(self):
        driver = webdriver.Chrome(executable_path="D:/Installers/chromedriver_v88/chromedriver.exe")
        driver.get("https://www.google.com/")
        title = driver.title
        self.assertEqual("Google", title, "Webpage title is not as expected")
        self.assertNotEqual("Google", title, "Webpage title is not as expected")
        driver.quit()


if __name__ == "__main__":
    unittest.main()
