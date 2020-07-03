from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("http://demo.automationtesting.in/")

driver.implicitly_wait(5)

driver.maximize_window()

driver.find_element(By.ID, "enterimg").click()

parent_ele = driver.find_element(By.LINK_TEXT, "SwitchTo")

hover_ele = ActionChains(driver).move_to_element(parent_ele).perform()

alert_ele = ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, "Alerts")).perform()
driver.find_element(By.LINK_TEXT, "Alerts").click()

# alerts handling
# driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()

# driver.switch_to.alert.accept()

# time.sleep(10)
# ul_ele = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/ul")
# items = ul_ele.find_elements(By.TAG_NAME, "li")
#
# for i in items:
#     print(i.text)


# ele = driver.find_element(By.XPATH, "//a[contains(text(),'Alert with OK & Cancel')]")
# # ActionChains(driver).move_to_element(ele).perform()
# ele.click()
#
# alert_element = driver.find_element(By.XPATH, "//*[@id='CancelTab']/button")
# alert_element.click()
#
# alert = WebDriverWait(driver, 10).until(EC.alert_is_present(), 'Timed out')

ele = driver.find_element(By.XPATH, "//a[contains(text(),'Alert with Textbox')]").click()

driver.find_element(By.XPATH, "//*[@id='Textbox']/button").click()

driver.switch_to.alert.send_keys("Lakshmi")

driver.switch_to.alert.accept()

driver.close()


