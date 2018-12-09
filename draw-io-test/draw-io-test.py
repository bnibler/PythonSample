from selenium.webdriver.common.keys import Keys
import os
from time import sleep
from helpers import WebdriverHelper
#from xml-parser import XmlParser

def drawTest():
    try:
        externalFilesPath = os.path.join(os.path.realpath(os.getcwd()), '..', 'external_files')
        diagramFileName = 'file_output_test_pattern.xml'

        webdriver = openDrawIo(externalFilesPath)
        createDiagram(webdriver, diagramFileName)
        createTestImage(webdriver)
        downloadDiagram(webdriver)

    finally:
        sleep(10)
        webdriver.quit()


def openDrawIo(externalFilesPath):
    #Create driver
    driver = WebdriverHelper(externalFilesPath)
    #navigate to starting page
    driver.browserGet("https://draw.io")
    assert "draw.io" in driver.browserTitle()
    return driver


def createDiagram(driver, diagramName):
    deviceButtonLocator = '//a[@title="Device"]'
    createNewDiagramLocator = '//button[contains(@class, geBigButton) and text() = "Create New Diagram"]'
    filenameInputLocator = '//div[@class="geDialog"]//input'
    createDiagramButtonLocator = '//div[@class="geDialog"]//button[text() = "Create"]'

    #choose output
    driver.clickElement(deviceButtonLocator)

    #choose create new diagram option
    driver.clickElement(createNewDiagramLocator)

    #set file name and create diagram
    driver.inputText(filenameInputLocator, diagramName)
    driver.clickElement(createDiagramButtonLocator)


def createTestImage(driver):
    paperSizeInputParentLocator = '//div[contains(@class, "geFormatContainer")]//div[div/text() = "Paper Size"]'
    paperSizeDropdownCustomOptionLocator = paperSizeInputParentLocator + '/select/option[@value="custom"]'
    widthInputLocator = paperSizeInputParentLocator + '//input[@style="text-align: right;"][1]'
    heightInputLocator = paperSizeInputParentLocator + '//input[@style="text-align: right;"][2]'
    #Shapes tab + button locators
    arrowShapeTabLocator = '//div[@class = "geSidebarContainer"]//a[@class="geTitle" and text() = "Arrows"][2]'
    arrowShapeButtonsLocator = arrowShapeTabLocator + '/following-sibling::div[1]//a'
    basicShapeTabLocator = '//div[@class = "geSidebarContainer"]//a[@class="geTitle" and text() = "Basic"]'
    basicShapeButtonsLocator = basicShapeTabLocator + '/following-sibling::div[1]//a'
    #Diagram content locators
    diagramContainerLocator = '//div[@class="geDiagramContainer geDiagramBackdrop"]'
    arrowSvgWrapperLocator = diagramContainerLocator + '//*[name() = "svg"]//*[contains(@style, "visibility: visible;")][1]'
    smileySvgWrapperLocator = diagramContainerLocator + '//*[name() = "svg"]//*[contains(@style, "visibility: visible;")][2]'
    #resize/reposition control locators
    controlNodesLocator = diagramContainerLocator + '//*[name() = "svg"]/*[name() = "g"]/*[name() = "g"][3]'
    eResizeNodeLocator = controlNodesLocator + '/*[contains(@style, "cursor: e-resize;")]'
    moveNodeLocator = controlNodesLocator + '/*[contains(@style, "cursor: move;")]'


    #Set Diagram size
    ##Set size to custom
    driver.clickElement(paperSizeDropdownCustomOptionLocator)
    #width
    driver.clickElement(widthInputLocator)
    driver.doubleClickElement(widthInputLocator)
    driver.inputText(widthInputLocator, '4' + Keys.ENTER)
    #height
    driver.clickElement(heightInputLocator)
    driver.doubleClickElement(heightInputLocator)
    driver.inputText(heightInputLocator, '4' + Keys.ENTER)

    #Add shapes to diagram
    ##Arrow
    driver.clickElement(arrowShapeTabLocator)
    driver.clickNthElement(arrowShapeButtonsLocator, 25)

    ##Smiley face
    driver.clickElement(basicShapeTabLocator)
    driver.clickNthElement(basicShapeButtonsLocator, 43)

    #Adjust image
    ##Resize arrow
    driver.clickElement(arrowSvgWrapperLocator)
    driver.dragAndDropByOffset(eResizeNodeLocator, 150, 0)

    ##Reposition elements
    ###Arrow
    driver.clickElement(arrowSvgWrapperLocator)
    driver.dragAndDropByOffset(moveNodeLocator, 55, 40)

    ###Smiley
    driver.clickElement(smileySvgWrapperLocator)
    driver.dragAndDropByOffset(moveNodeLocator, 130, -60)


def downloadDiagram(driver):
    saveAlertLocator = '//div[@class="geStatusAlert" and text() = "Unsaved changes. Click here to save."]'
    driver.clickElement(saveAlertLocator)



if __name__ == '__main__':
  drawTest()
