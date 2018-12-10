from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class WebdriverHelper(object):
    driver = None

    def browserGet(self, url):
        self.driver.get(url)

    def clearAlert(self):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.alert_is_present())
            alertMsg = self.driver.switch_to.alert
            alertMsg.accept()
        except TimeoutException:
            print('')

    def browserTitle(self):
        return self.driver.title

    def clickElement(self, locator):
            element = self.getElementByXpath(locator)
            element.click()

    def inputText(self, locator, text):
        self.getElementByXpath(locator).send_keys(text)

    def getElementByXpath(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

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

    def getElementValue(self, locator):
        element = self.getElementByXpath(locator)
        return element.get_attribute('value')

    def quit(self):
        self.driver.quit()

    def __init__(self, savePath):
        chromeOptions = webdriver.ChromeOptions()
        chromePrefs = {"download.default_directory": savePath, 'safebrowsing.enabled': 'false'}
        chromeOptions.add_experimental_option("prefs", chromePrefs)
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.implicitly_wait(10)
