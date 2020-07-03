from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("http://demo.automationtesting.in/")

driver.maximize_window()

driver.find_element(By.ID, "enterimg").click()

# input boxes
inputboxes = driver.find_elements_by_tag_name("form-control ng-pristine ng-invalid ng-invalid-required ng-touched")
print("No of inputboxes", len(inputboxes))

fname = driver.find_element(By.XPATH, "//input[@ng-model='FirstName']")
fname.clear()
fname.send_keys("lakshmi")

lname = driver.find_element(By.XPATH, "//input[@ng-model='LastName']")
lname.clear()
lname.send_keys("ch")

email = driver.find_element(By.XPATH, "//input[@ng-model='EmailAdress']")
email.clear()
email.send_keys("lakshmi@test.com")

phone = driver.find_element(By.XPATH, "//input[@ng-model='Phone']")
phone.clear()
phone.send_keys("2132424234")

# radio buttons
bstatus = driver.find_element(By.XPATH, "//input[@value='FeMale']").is_selected()
print("Before gender selected or not", bstatus)
driver.find_element(By.XPATH, "//input[@value='FeMale']").click()

astatus = driver.find_element(By.XPATH, "//input[@value='FeMale']").is_selected()
print("After gender selected or not", astatus)

# checkboxes
driver.find_element_by_id("checkbox1").click()
driver.find_element_by_id("checkbox3").click()

status = driver.find_element_by_id("checkbox1").is_enabled()
print("checkbox enabled or not", status)

# handling dropdown
drpdwn = Select(driver.find_element_by_id("countries"))

# drpdwn.select_by_visible_text("Guatemala")

# drpdwn.select_by_index(1)

drpdwn.select_by_value("India")

# count of no of options
all_opt = drpdwn.options
print("Count of options in the dropdown",len(all_opt))

# print all options
for i in all_opt:
    print("all options text", i.text)


# driver.close()

