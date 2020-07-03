from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver_83.exe")

driver.get("http://testautomationpractice.blogspot.com/")

# driver.save_screenshot("E:\selenium\Seleniumwithpython\Screenshots\homepage.jpeg")

driver.get_screenshot_as_file("E:\selenium\Seleniumwithpython\Screenshots\homepage2.jpg")

# driver.get_screenshot_as_png("E:\selenium\Seleniumwithpython\Screenshots\homepage3.jpg")