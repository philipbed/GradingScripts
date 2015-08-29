"""
Script that will sign into myCourses and download the
zip files of all selected students

Author: Philip Bedward
"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#open Chrome and load myCourses
browser = webdriver.Chrome('C:\chromedriver.exe')
browser.get('https://mycourses.rit.edu')

#login to myCourses
login_part_one = browser.find_element_by_name('username')
login_part_two = browser.find_element_by_name('password')
username = input("What is your username ?: ")
password = input("What is your password ?: ")
login_part_one = login_part_one.send_keys(username)
login_part_two = login_part_two.send_keys(password)
submit = browser.find_element_by_name("f_submit")
submit.click()

#navigate to the proper Lab and filter the students
input("Please navigate to proper Lab page")

#Check all students 
check_box = browser.find_element_by_name("z_h_cb_sa")
check_box.click()
download_button = browser.find_element_by_class_name("di_t")
download_button.click()

#handle pop-up window
input("press enter after pop up window appears")
browser.switch_to_window(browser.window_handles[1]) # problems switching to pop-up window
zip_link = browser.find_element_by_partial_link_text("Lab")
#zip_link.click()
                                                               
