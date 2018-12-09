from selenium.webdriver.common.keys import Keys
import os
import lxml
from time import sleep
from helpers import WebdriverHelper

externalFilesPath = os.path.join(os.path.realpath(os.getcwd()), 'external_files')
driver = WebdriverHelper(externalFilesPath)

#login flow
driver.browserGet("https://draw.io")
assert "draw.io" in driver.browserTitle()

#choose output
deviceButtonLocator = '//a[@title="Device"]'
driver.clickElement(deviceButtonLocator)

#choose create
createNewDiagramLocator = '//button[contains(@class, geBigButton) and text() = "Create New Diagram"]'
driver.clickElement(createNewDiagramLocator)

#set file name and create diagram
filenameInputLocator = '//div[@class="geDialog"]//input'
driver.inputText(filenameInputLocator, 'file_output_test_pattern.xml')

createDiagramButtonLocator = '//div[@class="geDialog"]//button[text() = "Create"]'
driver.clickElement(createDiagramButtonLocator)

#Set Diagram size
paperSizeInputParentLocator = '//div[contains(@class, "geFormatContainer")]//div[div/text() = "Paper Size"]'
paperSizeDropdownCustomOptionLocator = paperSizeInputParentLocator + '/select/option[@value="custom"]'
driver.clickElement(paperSizeDropdownCustomOptionLocator)

sizeInputLocator = paperSizeInputParentLocator + '//input[@style="text-align: right;"]'
driver.clickElement(sizeInputLocator+'[1]')

driver.doubleClickElement(sizeInputLocator+'[1]')
driver.inputText(sizeInputLocator+'[1]', '4' + Keys.ENTER)

driver.clickElement(sizeInputLocator+'[2]')
driver.doubleClickElement(sizeInputLocator+'[2]')
driver.inputText(sizeInputLocator+'[2]', '4' + Keys.ENTER)

#Add shapes to diagram
##Arrow
arrowShapeTabLocator = '//div[@class = "geSidebarContainer"]//a[@class="geTitle" and text() = "Arrows"][2]'
driver.clickElement(arrowShapeTabLocator)

arrowShapeButtonsLocator = arrowShapeTabLocator + '/following-sibling::div[1]//a'
driver.clickNthElement(arrowShapeButtonsLocator, 25)

##Smiley face
basicShapeTabLocator = '//div[@class = "geSidebarContainer"]//a[@class="geTitle" and text() = "Basic"]'
driver.clickElement(basicShapeTabLocator)


basicShapeButtonsLocator = basicShapeTabLocator + '/following-sibling::div[1]//a'
driver.clickNthElement(basicShapeButtonsLocator, 43)

#Adjust image
diagramContainerLocator = '//div[@class="geDiagramContainer geDiagramBackdrop"]'
arrowSvgWrapperLocator = diagramContainerLocator + '//*[name() = "svg"]//*[contains(@style, "visibility: visible;")][1]'
smileySvgWrapperLocator = diagramContainerLocator + '//*[name() = "svg"]//*[contains(@style, "visibility: visible;")][2]'
resizeNodesLocator = diagramContainerLocator + '//*[name() = "svg"]/*[name() = "g"]/*[name() = "g"][3]'

##Resize arrow
driver.clickElement(arrowSvgWrapperLocator)

eResizeNodeLocator = resizeNodesLocator + '/*[contains(@style, "cursor: e-resize;")]'
driver.dragAndDropByOffset(eResizeNodeLocator, 150, 0)

##Reposition elements
###Arrow
driver.clickElement(arrowSvgWrapperLocator)

moveNodeLocator = resizeNodesLocator + '/*[contains(@style, "cursor: move;")]'
driver.dragAndDropByOffset(moveNodeLocator, 55, 40)

###Smiley
driver.clickElement(smileySvgWrapperLocator)

moveNodeLocator = resizeNodesLocator + '/*[contains(@style, "cursor: move;")]'
driver.dragAndDropByOffset(moveNodeLocator, 130, -60)

#Download
saveAlertLocator = '//div[@class="geStatusAlert" and text() = "Unsaved changes. Click here to save."]'
driver.clickElement(saveAlertLocator)


sleep(15)
driver.quit()


#Set d/l location
#Create webdriver
#choose drive
#Create diagram
#Name it
#Create button
##Page contains canvas and left bar
#set size
#Add shapes
###Modify shapes for funsies
#Save
#Screenshot
#Parse out compressed
#Compare size
#Go to decompress
#Decompress
#compare data to known

###############
#Decorators
##Nav ops -- wait for page to stop loading
##Change op -- built-in delay
##Poll on presence
######
#Challenge implements
##XML parse
##Compare content to known