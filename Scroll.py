from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get(r"http://demo.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id("enterimg").click()
driver.find_element_by_link_text("Practice Site").click()

# driver.execute_script("window.scrollBy(0,1000)", "") # scroll down by pixel

# element = driver.find_element_by_xpath("//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[2]")
# driver.execute_script("arguments[0].scrollIntoView();", element)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")



driver.close()