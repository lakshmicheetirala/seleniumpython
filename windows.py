from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# import HTMLTestRunner

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("http://demo.automationtesting.in/")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.ID, "enterimg").click()

parent_ele = driver.find_element(By.LINK_TEXT, "SwitchTo")

hover_ele = ActionChains(driver).move_to_element(parent_ele).perform()

alert_ele = ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, "Windows")).perform()
driver.find_element(By.LINK_TEXT, "Windows").click()


# time.sleep(10)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)

windows = driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    print(driver.title)

driver.quit()

