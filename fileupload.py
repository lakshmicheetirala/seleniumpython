from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")

driver.switch_to.frame(0)

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://Users/Lakshmi/Pictures/Screenshots/Screenshot (1).png")

print("done")

driver.close()

