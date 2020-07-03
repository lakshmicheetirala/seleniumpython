from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

click_ele = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)

actions.double_click(click_ele).perform()

print("double clicked")

driver.close()




