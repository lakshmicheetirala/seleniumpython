from selenium import webdriver
import time

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain, application/pdf") # mime type
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", r"E:\selenium\Seleniumwithpython\downloads")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(executable_path=r"E:\selenium\drivers\firefoxdriver\geckodriver.exe", firefox_profile=fp)

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
