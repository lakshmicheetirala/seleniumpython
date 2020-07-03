from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("http://www.newtours.demoaut.com/")

driver.implicitly_wait(5)  # time in seconds need to specify one time in the script
assert "Welcome: Mercury Tours" in driver.title

uname = driver.find_element_by_name("userName")
print("username displayed or not", uname.is_displayed())
print("username enabled or not", uname.is_enabled())


pwd = driver.find_element_by_name("password")
print("password displayed or not", pwd.is_displayed())
print("password displayed or not", pwd.is_enabled())

uname.send_keys("mercury")
pwd.send_keys("mercury")

driver.find_element_by_name("login").click()

time.sleep(5)
print("Roundtrip is selected or not", driver.find_element_by_css_selector("input[value='roundtrip']").is_selected())

print("Roundtrip is selected or not", driver.find_element_by_css_selector("input[value='oneway']").is_selected())

driver.close()


