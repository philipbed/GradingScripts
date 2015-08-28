import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('C:\chromedriver.exe')
browser.get('https://mycourses.rit.edu')
login_one = browser.find_element_by_name('username')
login_two = browser.find_element_by_name('password')
username = input("What is your username ?: ")
login_one = login_one.send_keys(username)


