from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class WebdriverHelper(object):
    driver = None

    def browserGet(self, url):
        self.driver.get("https://draw.io")

    def browserTitle(self):
        return self.driver.title

    def clickElement(self, locator):
            element = self.getElementByXpath(locator)
            element.click()

    def inputText(self, locator, text):
        self.getElementByXpath(locator).send_keys(text)

    def getElementByXpath(self, locator):
        try:
            element = self.driver.find_element(By.XPATH, locator)
            return element
        except NoSuchElementException:
            print('No matching element found - ' + locator)

    def getElementsByXpath(self, locator):
        elements = self.driver.find_elements(By.XPATH, locator)
        return elements

    def doubleClickElement(self, locator):
        element = self.getElementByXpath(locator)
        ActionChains(self.driver) \
            .double_click(element) \
            .perform()

    def clickNthElement(self, locator, nth):
        elements = self.getElementsByXpath(locator)
        elements[nth].click()

    def dragAndDropByOffset(self, locator, xOffset, yOffset):
        element = self.getElementByXpath(locator)
        ActionChains(self.driver) \
            .drag_and_drop_by_offset(element, xOffset, yOffset) \
            .perform()

    def quit(self):
        self.driver.quit()

    def __init__(self, savePath):
        chromeOptions = webdriver.ChromeOptions()
        chromePrefs = {"download.default_directory": savePath, 'safebrowsing.enabled': 'false'}
        chromeOptions.add_experimental_option("prefs", chromePrefs)
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.implicitly_wait(10)
