from selenium import webdriver

# driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

# driver = webdriver.Firefox(executable_path=r"E:\selenium\drivers\firefoxdriver\geckodriver.exe")

driver = webdriver.Ie(executable_path=r"E:\selenium\drivers\IEDriverServer_Win32_3.9.0\IEDriverServer.exe")

driver.get("http://demo.automationtesting.in/")

print(driver.title)

print(driver.current_url)

# print(driver.page_source)

driver.quit()
