import xlutils
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("https://dev.focalcxm.com/baton-client-v2/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//button[@ng-reflect-router-link='/login/2']").click()

path = r"E:\selenium\registration_data.xlsx"

rows = xlutils.getRowcount(path, "writedata")

for r in range(2, rows+1):
    username = xlutils.readData(path, "writedata", r, 1)
    password = xlutils.readData(path, "writedata", r, 2)
    driver.find_element_by_xpath("//input[@ng-reflect-placeholder='Email']").clear()
    driver.find_element_by_xpath("//input[@ng-reflect-placeholder='Email']").send_keys(username)
    driver.find_element_by_xpath("//input[@ng-reflect-placeholder='Password']").clear()
    driver.find_element_by_xpath("//input[@ng-reflect-placeholder='Password']").send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/app-root/div/login/block-ui/div/div[2]/div/button/span/span").click()
    time.sleep(4)
    if driver.current_url == "https://dev.focalcxm.com/baton-client-v2/#/dashboard":
        print("Test is passes")
        xlutils.writeData(path,"writedata", r, 3, "Test passed")
    else:
        print("test failed")
        xlutils.writeData(path,"writedata", r, 3, "Test failed")

    driver.get("https://dev.focalcxm.com/baton-client-v2/#/login/2")

driver.close()
