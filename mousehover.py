from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r"E:\selenium\drivers\chromedriver\chromedriver.exe")

driver.get("http://demo.automationtesting.in/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id("enterimg").click()

inter_ele = driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[6]/a")
drag_ele = driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[6]/ul/li[1]/a")
static_ele = driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[6]/ul/li[1]/ul/li[1]/a")

actions = ActionChains(driver)
actions.move_to_element(inter_ele).move_to_element(drag_ele).move_to_element(static_ele).click().perform()


