from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("http://www.newtours.demoaut.com/")

alllinks = driver.find_elements(By.TAG_NAME, "a")
print("Number of links present", len(alllinks))

for link in alllinks:
    print("link=================>", link.text)

# driver.find_element(By.LINK_TEXT, "SUPPORT").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "TER").click()
