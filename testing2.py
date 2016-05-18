from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
#driver.get("https://www.google.co.in/?gfe_rd=cr&ei=qYc5V9zUMs2L8QeX15Jg&gws_rd=ssl")
#assert "Google" in driver.title
#elem = driver.find_element_by_id("lst-ib")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#ele = driver.find_element_by_name("q")
#print ele.get_attribute('value')
#assert "No results found." not in driver.page_source

driver.get("http://pytest.org/dev/example/capture.html")
elem = driver.find_element_by_link_text("Usages and Examples")
elem.click()

driver.close()
