from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

driver.maximize_window()

right_click_ele = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

action = ActionChains(driver)

action.context_click(right_click_ele).perform()