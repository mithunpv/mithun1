import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Testing(unittest.TestCase):
	@classmethod
	def setup_class(cls):
		cls.driver=webdriver.Firefox()
		driver=cls.driver
	@pytest.mark.run(order=1)
	def testexam(self):
		driver=self.driver
		driver.get("http://www.w3schools.com/html/default.asp")
		ele=driver.find_element_by_xpath("//div[3]/div[2]/div/div/div[4]/a").click()
		time.sleep(5)
		a=driver.window_handles
		driver.switch_to_window(a[1])
		el=driver.find_element_by_xpath("//div[2]/ul/li[3]/button").click()
		print el.tag_name
		time.sleep(10)		
	

	@classmethod	
	def teardown_class(cls):
		cls.driver.close()

	
if __name__== "__main__":
	unittest.main()
