from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("http://demo.automationtesting.in/")

driver.implicitly_wait(5)

driver.maximize_window()

driver.find_element(By.ID, "enterimg").click()

parent_ele = driver.find_element(By.LINK_TEXT, "SwitchTo")

hover_ele = ActionChains(driver).move_to_element(parent_ele).perform()

alert_ele = ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, "Frames")).perform()
driver.find_element(By.LINK_TEXT, "Frames").click()

driver.switch_to.frame("SingleFrame")
driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("This is Single frame")

driver.switch_to.default_content()

driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()

# # driver.switch_to.frame(1)
# iframe = driver.find_elements(By.TAG_NAME, "iframe")
#
# for frame in iframe:
#     print(frame.text)

first = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
first_frame = driver.switch_to.frame(first)

second = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
second_frame = driver.switch_to.frame(second)

driver.find_element(By.XPATH, "/html/body/section/div/div/div/input").send_keys("Multiple frames")

driver.close()


