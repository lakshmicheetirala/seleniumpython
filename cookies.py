from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver_83.exe")

driver.get("https://www.amazon.in/")

# cookies = driver.get_cookies()
# print("All Cookies================>",len(cookies))
# print("All Cookie pairs================>",cookies)

cookie = {'name':'Mycookie', 'value': '123456789'}

driver.add_cookie(cookie)
cookies = driver.get_cookies()
print("All Cookies================>",len(cookies))
print("All Cookie pairs================>",cookies)

driver.delete_cookie('Mycookie')

cookies = driver.get_cookies()
print("All Cookies================>",len(cookies))
print("All Cookie pairs================>",cookies)

driver.delete_all_cookies()
cookies = driver.get_cookies()
print("All Cookies================>",len(cookies))
print("All Cookie pairs================>",cookies)
