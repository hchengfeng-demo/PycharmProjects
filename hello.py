# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0.1"
caps["deviceName"] = "OPPO_R9s"
caps["appPackage"] = "cn.com.nbcard"
caps["appActivity"] = ".base.ui.SplashActivity"
caps["resetKeybroad"] = True
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

time.sleep(3)

TouchAction(driver).press(x=988, y=835).move_to(x=92, y=883).release().perform()

TouchAction(driver).press(x=988, y=857).move_to(x=66, y=861).release().perform()

TouchAction(driver).press(x=1006, y=835).move_to(x=31, y=870).release().perform()

el1 = driver.find_element_by_id("cn.com.nbcard:id/finishBtn")
el1.click()
el2 = driver.find_element_by_id("cn.com.nbcard:id/commitButton")
el2.click()

el4 = driver.find_element_by_id("cn.com.nbcard:id/civ_person_login")
el4.click()
el5 = driver.find_element_by_id("cn.com.nbcard:id/userInputEdt")
el5.send_keys("17512074988")
el6 = driver.find_element_by_id("cn.com.nbcard:id/pwdinputEdt")
el6.send_keys("huang920724")
el7 = driver.find_element_by_id("cn.com.nbcard:id/finishBtn")
el7.click()
el8 = driver.find_element_by_id("cn.com.nbcard:id/meTabIcon")
el8.click()
el9 = driver.find_element_by_id("cn.com.nbcard:id/gaLay")
el9.click()
el10 = driver.find_element_by_id("cn.com.nbcard:id/backBtn")
el10.click()
el11 = driver.find_element_by_id("cn.com.nbcard:id/settingsLay")
el11.click()
el12 = driver.find_element_by_id("cn.com.nbcard:id/exitAccountBtn")
el12.click()

driver.quit()
