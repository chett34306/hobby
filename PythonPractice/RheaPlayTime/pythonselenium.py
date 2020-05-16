from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
from bs4 import BeautifulSoup
import requests

#driver = webdriver.Chrome("/Users/mdevidi/Desktop/Praveen/python/RheaPlayTime/chromedriver")
driver = webdriver.Chrome("C:\\Users\\pchettypally\\Documents\\Visual Studio 2017\\Projects\\PythonPractice\\RheaPlayTime\\chromedriver.exe")

def sendkeysclick():
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
    messageField.send_keys("Hello World!")
    submitButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
    submitButton.click()
    valueA = driver.find_element_by_xpath('//*[@id="sum1"]')
    valueA.send_keys('10')
    valueB = driver.find_element_by_xpath('//*[@id="sum2"]')
    valueB.send_keys('20')
    sumButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
    sumButton.click()

def dragdrop():
    driver.maximize_window()
    driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-1.html')
    source = driver.find_element_by_xpath('//*[@id="box4"]')
    dest = driver.find_element_by_xpath('//*[@id="dropBox"]')
    actions = ActionChains(driver)
    actions.drag_and_drop(source, dest).perform()

def redfinscrap():
    driver.maximize_window()
    response = requests.get('https://www.redfin.com/zipcode/98029')
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='ReactDataTable subrow')
    print(items)

dragdrop()
sendkeysclick()
# redfinscrap()