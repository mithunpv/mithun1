from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.w3schools.com/")
assert "W3" in driver.title
elem = driver.find_element_by_tag_name("title")
print elem.get_attribute("innerHTML")
driver.close()
