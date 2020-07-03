from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("http://www.newtours.demoaut.com/")  # firstsite

print("First web site", driver.title)

driver.get("http://demo.automationtesting.in/")

print("Second web site", driver.title)

driver.back()

print("browser navigated back", driver.title)

driver.forward()

print("browser navigated fwd", driver.title)

driver.close()







