from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeopts = Options()
chromeopts.add_experimental_option("prefs",{"download.default_directory":"E:\selenium\Seleniumwithpython\downloads"})

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe", options=chromeopts)

driver.get("http://demo.automationtesting.in/")

driver.maximize_window()

driver.implicitly_wait(5)

print("maximized")

driver.find_element_by_id("enterimg").click()


driver.find_element_by_link_text("More").click()

driver.find_element_by_link_text("File Download").click()


driver.find_element_by_link_text("Download").click()

print("donwloaded")

driver.find_element_by_id("textbox").send_keys("testing donwload file")
driver.find_element_by_id("createTxt").click()
time.sleep(2)
driver.find_element_by_id("link-to-download").click()

print("downloaded text file")

driver.find_element_by_id("pdfbox").send_keys("generating pdf")
driver.find_element_by_xpath("//*[@id='createPdf']").click()
driver.find_element_by_link_text("Download").click()

print("PDF Downloaded")
