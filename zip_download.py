"""
Script that will sign into myCourses and download the
zip files of all selected students

Author: Philip Bedward
"""
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#open Chrome and load myCourses
##browser = webdriver.Chrome('C:\chromedriver.exe')
##browser.get('https://mycourses.rit.edu')

# open Firefox and load myCourses
def login():
    """
    Opens the Firefox web browser loads myCourses and prompts the user to enter
    their login credentials and clicks the submit button
    :return:
    """

    browser = webdriver.Firefox()


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
def select_all():
    """
    Prompts the user to navigate to the proper lab page
    then selects all students and clicks the download
    button.
    :return:
    """
    input("Please navigate to proper Lab page")

    #Check all students
    print(list(browser.window_handles))
    check_box = browser.find_element_by_name("z_h_cb_sa")
    check_box.click()
    download_button = browser.find_element_by_class_name("di_t")
    download_button.click()


#handle pop-up window
def change_windows():
    """
    Gets the popup window's handle pattern and sets
    that as the current window handle
    """
    # Store sll of the window handles into a list
    handles = list(browser.window_handles)

    # Make sure there are two window handles
    print("There are two window handles: ",len(handles)==2)

    # Remove the current window handle from the list
    handles.remove(browser.current_window_handle)

    # Switch to the window handle of the popup window
    browser.switch_to.window(handles[0])


    print(browser.current_url) # double check the url

# Switches to proper window but cannot find link element

def download_all():
    """
    Clicks the download link for all zip files
    :return:
    """
    try:
        wait = WebDriverWait(browser,100)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#z_b > a")))
        zip_link = browser.find_element_by_css_selector("#z_b > a")

    except Exception as e:
        print(e)



                                                              
