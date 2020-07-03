from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("https://www.expedia.com")

driver.maximize_window()

driver.implicitly_wait(10)
driver.find_element(By.ID, "tab-flight-tab-hp").click()

# time.sleep(5)
driver.find_element(By.ID, "flight-origin-hp-flight").clear()
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("Hyderabad (HYD-Rajiv Gandhi Intl.)")

# time.sleep(5)
driver.find_element(By.ID, "flight-destination-hp-flight").clear()
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("Goa (GOI-Dabolim)")

# time.sleep(5)
driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("05/26/2020")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("05/31/2020")

# time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# explicit wait

try:
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH, "//*[@id='stopFilter_stops-1']"))
    element.click()

finally:
    driver.close()

