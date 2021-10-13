from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as py
'''
Author: Allen Hsu 
Date: 2021/09/10
Input:
Output:
'''



#Define the browser and use chromedriver to open it -> maximize window -> go to address
browser = webdriver.Chrome(executable_path='Dependency/chromedriver')
browser.maximize_window()
browser.get('http://nonstopdb.dkfz.de/')

#Wait the server to load the element and click
element_1 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sidebar.menu"]/li[3]/a')))
print('YES!')
element_1.click()
#locate to the region box
element_2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID,'regionTab.region-currInput')))
print('YES!')
element_2.click()
py.typewrite('1-248956422',interval=0.01)
#locate to the submit button
element_3 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID,'regionTab.submit')))
print('YES!')
element_3.click()

#locate to download button
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="DataTables_Table_0_wrapper"]/div[4]/div[1]/div/table/thead/tr/th[2]')))

element_4 = browser.find_element_by_id('regionTab.table-DownloadAll')
element_4.click()

#locate to chromosome box
time.sleep(3)
for i in range(24):
    element_5 = browser.find_element_by_xpath('//*[@id="shiny-tab-regionTab"]/div[1]/div[1]/div/div/div/div[1]')
    element_5.click()
    py.press('down')
    py.press('return')

    #locate to download button
    time.sleep(3)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") 

    element_4 = browser.find_element_by_id('regionTab.table-DownloadAll')

    actions = ActionChains(browser)
    actions.move_to_element(element_4).perform()

    element_4.click()

    time.sleep(3)

    browser.execute_script("window.scrollTo(0, 0)") 