import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class test2(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "maverick1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/accounts/login/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com")
       assert "Logged In"
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/about/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(1)
       driver.find_element_by_xpath("//*[@id='content']/table/tbody/tr[2]/td[12]/a").click()
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer/1/edit/")
       time.sleep(1)
       driver.find_element_by_id("id_zipcode").clear()
       driver.find_element_by_id("id_zipcode").send_keys("68122")
       time.sleep(2)
       driver.find_element_by_xpath("//*[@id='content']/div/form/button").click()
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer/new/")
       elem = driver.find_element_by_id("id_customer_id")
       elem.send_keys("12")
       elem = driver.find_element_by_id("id_customer_name")
       elem.send_keys("Nancy")
       elem = driver.find_element_by_id("id_city")
       elem.send_keys("Omaha")
       elem = driver.find_element_by_id("id_state")
       elem.send_keys("NE")
       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys("68127")
       elem = driver.find_element_by_id("id_contact_details")
       elem.send_keys("4029959072")
       elem = driver.find_element_by_id("id_email_address")
       elem.send_keys("nancy_jain@yhaoo.com")
       elem = driver.find_element_by_id("id_customer_room_no")
       elem.send_keys("126")
       elem = driver.find_element_by_id("id_customer_stay_start_date")
       elem.send_keys()
       elem = driver.find_element_by_id("id_customer_stay_end_date")
       elem.send_keys()
       elem = driver.find_element_by_xpath("//*[@id='content']/form/button")
       elem.click()
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer/12/delete")
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customerservice_list/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customerservice/2/edit/")
       time.sleep(1)
       driver.find_element_by_id("id_service_charge").clear()
       driver.find_element_by_id("id_service_charge").send_keys("12.50")
       time.sleep(2)
       driver.find_element_by_xpath("//*[@id='content']/div/form/button").click()
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customer_list/")
       time.sleep(3)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customerservice/new/")
       time.sleep(1)
       select = Select(driver.find_element_by_xpath("//*[@id='id_customer_name']"))
       select.select_by_index(1)
       select = Select(driver.find_element_by_xpath("//*[@id='id_service_category']"))
       select.select_by_index(2)
       driver.find_element_by_id("id_description").send_keys("Cleaning")
       driver.find_element_by_id("id_service_charge").send_keys("12")
       time.sleep(1)
       driver.find_element_by_xpath("//*[@id='content']/form/button").click()
       time.sleep(3)
       driver.get(" https://assignment4-vishekha-8220.herokuapp.com/customerservice/32/delete/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/customerservice_list/")
       time.sleep(3)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/roomstatus_list/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/roomstatus/123/edit/")
       time.sleep(1)
       self.driver.find_element_by_xpath("//input[@name='room_availability']").click()
       driver.find_element_by_xpath("//*[@id='content']/div/form/button").click()
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/roomstatus/new/")
       time.sleep(2)
       select = Select(driver.find_element_by_xpath("//*[@id='id_room_type']"))
       select.select_by_index(1)
       driver.find_element_by_id("id_room_no").send_keys("104")
       driver.find_element_by_id("id_room_description").send_keys("Smoking Room")
       self.driver.find_element_by_xpath("//input[@name='room_availability']").click()
       time.sleep(1)
       driver.find_element_by_xpath("//*[@id='content']/form/button").click()
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/roomstatus_list/")
       time.sleep(2)
       driver.get(" https://assignment4-vishekha-8220.herokuapp.com/roomstatus/104/delete/")
       time.sleep(1)
       driver.get("https://assignment4-vishekha-8220.herokuapp.com/roomstatus_list/")
       time.sleep(2)
       driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[2]").click()
       time.sleep(2)


def tearDown(self):
       self.driver.close()
       time.sleep(1)

if __name__ == "__main__":
   unittest.main()

