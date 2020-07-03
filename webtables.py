from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get(r"http://demo.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_id("enterimg").click()
driver.find_element_by_link_text("WebTable").click()

row = driver.find_elements_by_xpath("//div[@class='ui-grid-row ng-scope']")
print(row)
rows = len(row)
print("Rows of the table===========>", rows)

col = driver.find_elements_by_xpath("//div[@col='col']")
print(col)
cols = len(col)
print("coloumns of the table=========>", cols)

# element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[@ng-class='{ 'ui-grid-row-header-cell': col.isRowHeader }']")))
element = driver.find_elements_by_xpath("//div[@class='ui-grid-cell-contents ng-binding ng-scope']")
print("length of the element", len(element))
for i in range(len(element)):
    print(element[i].text)
    # print("\n")

# for r in range(2,rows+1):
# 	for c in range(1,cols+1):
# 		element = driver.find_element(By.XPATH, "//div[@class='ui-grid-cell-contents ng-binding ng-scope']")
# 		value=element.text
# 		print(value,end=" ")
# 	print()
driver.quit()
