from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import lxml
from time import sleep

externalFilesPath = os.path.join(os.path.realpath(os.getcwd()), 'external_files')

chromeOptions = webdriver.ChromeOptions()
chromePrefs = {"download.default_directory": externalFilesPath, 'safebrowsing.enabled': 'false'}
chromeOptions.add_experimental_option("prefs", chromePrefs)
driver = webdriver.Chrome(options=chromeOptions)
driver.implicitly_wait(10)

#login flow
driver.get("https://draw.io")
assert "draw.io" in driver.title

#choose output
deviceButtonLocator = '//a[@title="Device"]'
deviceButton = driver.find_element(By.XPATH, deviceButtonLocator)
deviceButton.click()

#choose create
createNewDiagramLocator = '//button[contains(@class, geBigButton) and text() = "Create New Diagram"]'
newDiagramButton = driver.find_element(By.XPATH, createNewDiagramLocator)
newDiagramButton.click()

#set file name and create diagram
filenameInputLocator = '//div[@class="geDialog"]//input'
filenameInput = driver.find_element(By.XPATH, filenameInputLocator)
filenameInput.send_keys('file_output_test_pattern.xml')

createDiagramButtonLocator = '//div[@class="geDialog"]//button[text() = "Create"]'
createDiagramButton = driver.find_element(By.XPATH, createDiagramButtonLocator)
createDiagramButton.click()

#Set Diagram size
paperSizeInputParentLocator = '//div[contains(@class, "geFormatContainer")]//div[div/text() = "Paper Size"]'
paperSizeDropdownCustomOptionLocator = paperSizeInputParentLocator + '/select/option[@value="custom"]'
paperSizeDropdownCustomOption = driver.find_element(By.XPATH, paperSizeDropdownCustomOptionLocator)
paperSizeDropdownCustomOption.click()

sizeInputLocator = paperSizeInputParentLocator + '//input[@style="text-align: right;"]'
sizeInput = driver.find_element(By.XPATH, sizeInputLocator+'[1]')
sizeInput.click()
ActionChains(driver)\
    .double_click(sizeInput)\
    .perform()
sizeInput.send_keys('4' + Keys.ENTER)

sizeInput2 = driver.find_element(By.XPATH, sizeInputLocator+'[2]')
sizeInput2.click()
ActionChains(driver)\
    .double_click(sizeInput2)\
    .perform()
sizeInput2.send_keys('4' + Keys.ENTER)

#Add shapes to diagram
##Arrow
arrowShapeTabLocator = '//div[@class = "geSidebarContainer"]//a[@class="geTitle" and text() = "Arrows"][2]'
arrowShapeTab = driver.find_element(By.XPATH, arrowShapeTabLocator)
arrowShapeTab.click()

arrowShapeButtonsLocator = arrowShapeTabLocator + '/following-sibling::div[1]//a'
arrowShapeButtons = driver.find_elements(By.XPATH, arrowShapeButtonsLocator)
arrowShapeButtons[25].click()

##Smiley face
basicShapeTabLocator = '//div[@class = "geSidebarContainer"]//a[@class="geTitle" and text() = "Basic"]'
basicShapeTab = driver.find_element(By.XPATH, basicShapeTabLocator)
basicShapeTab.click()

basicShapeButtonsLocator = basicShapeTabLocator + '/following-sibling::div[1]//a'
basicShapeButtons = driver.find_elements(By.XPATH, basicShapeButtonsLocator)
basicShapeButtons[43].click()

#Adjust image
diagramContainerLocator = '//div[@class="geDiagramContainer geDiagramBackdrop"]'
arrowSvgWrapperLocator = diagramContainerLocator + '//*[name() = "svg"]//*[contains(@style, "visibility: visible;")][1]'
smileySvgWrapperLocator = diagramContainerLocator + '//*[name() = "svg"]//*[contains(@style, "visibility: visible;")][2]'
resizeNodesLocator = diagramContainerLocator + '//*[name() = "svg"]/*[name() = "g"]/*[name() = "g"][3]'

##Resize arrow
arrowSvgWrapper = driver.find_element(By.XPATH, arrowSvgWrapperLocator)
arrowSvgWrapper.click()
eResizeNodeLocator = resizeNodesLocator + '/*[contains(@style, "cursor: e-resize;")]'
eResizeNode = driver.find_element(By.XPATH, eResizeNodeLocator)
ActionChains(driver)\
    .drag_and_drop_by_offset(eResizeNode, 150, 0)\
    .perform()

##Reposition elements
###Arrow
arrowSvgWrapper = driver.find_element(By.XPATH, arrowSvgWrapperLocator)
arrowSvgWrapper.click()

moveNodeLocator = resizeNodesLocator + '/*[contains(@style, "cursor: move;")]'
moveNode = driver.find_element(By.XPATH, moveNodeLocator)

ActionChains(driver)\
    .drag_and_drop_by_offset(moveNode, 55, 40)\
    .perform()

###Smiley
smileySvgWrapper = driver.find_element(By.XPATH, smileySvgWrapperLocator)
smileySvgWrapper.click()

moveNodeLocator = resizeNodesLocator + '/*[contains(@style, "cursor: move;")]'
moveNode = driver.find_element(By.XPATH, moveNodeLocator)

ActionChains(driver)\
    .drag_and_drop_by_offset(moveNode, 130, -60)\
    .perform()

#Download
saveAlertLocator = '//div[@class="geStatusAlert" and text() = "Unsaved changes. Click here to save."]'
saveAlert = driver.find_element(By.XPATH, saveAlertLocator)
saveAlert.click()

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