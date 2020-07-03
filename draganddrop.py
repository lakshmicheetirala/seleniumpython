from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()
print("maximized")

source_ele = driver.find_element_by_id("draggable")
print("found source")

target_ele = driver.find_element_by_id("droppable")

actions = ActionChains(driver)

print(actions)

actions.drag_and_drop(source_ele, target_ele).perform()

driver.close()

