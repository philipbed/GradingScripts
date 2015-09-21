__author__ = 'Phil'
"""
Script that will sign into myCourses, navigate
to the proper Lab page, open the popup window
that contains the zip file of all the students labs
and downloads them.

Author: Philip Bedward
Date: 9/8/2015
"""

from selenium import webdriver


class Driver:

    def __init__( self, driver=webdriver.Firefox()):
        """
        initializes the WebDriver's properties

        driver - preset to the Firefox web browser
        :return:
        """
        self.browser = driver
        self.url = driver.current_url
        self.browser.implicitly_wait(10)

    def open( self, link ):
        """
        Opens the browser of choice and directs you to the site of choice.

        link - the website destination desired.
        """
        """
        :param link:
        :return:
        """
        self.browser.get(link)

    def login( self ):
        """
        Loads myCourses and prompts the user to enter
        their login credentials and clicks the submit button
        :return:
        """

        #login to myCourses
        input("Please type in your login credential then press enter")
        submit = self.browser.find_element_by_name("f_submit")
        submit.click()



    def select_all(self):
        """
        Prompts the user to navigate to the proper lab page
        then selects all students and clicks the download
        button.
        :return:
        """


        #Check all students
        check_box = self.browser.find_element_by_name("z_h_cb_sa")

        check_box.click()

        download_button = self.browser.find_element_by_class_name("di_t")

        download_button.click()


    #handle pop-up window
    def change_windows(self):
        """
        Gets the popup window's handle pattern and sets
        that as the current window handle
        """

        # Store all of the window handles into a list
        handles = self.browser.window_handles

        # Make sure there are two window handles

        # Remove the current window handle from the list
        handles.remove( self.browser.current_window_handle )

        # Switch to the window handle of the popup window
        self.browser.switch_to.window( self.browser.window_handles[1] )


    def download_all(self):
        """
        Clicks the download linke that is present on the page.
        :return:
        """
        """
        :return:
        """
        frames = self.browser.find_elements_by_tag_name('frame')

        #Choose the second frame in the popup window.
        frame = frames[1]
        self.browser.switch_to.frame(frame)

        download_link = self.browser.find_element_by_css_selector('span.dfl>a')
        download_link.click()


    def navigate_to_lab(self):
        """
        Will navigate to the proper lab page using user input.
        """
        input("Press 'Enter' after you login: ")

        # Clicks the menu dropdown for the 'Select a course' link
        flyout = self.browser.find_element_by_css_selector("a.d2l-menuflyout-opener.d2l-clickable")
        flyout.click()

        # Clicks the link to go to the CSI page
        computer_science_one = self.browser.find_element_by_partial_link_text("Computer Science I")
        computer_science_one.click()

        # Clicks the dropbox link in the navigation bar
        navbar = self.browser.find_elements_by_css_selector("a.d2l-navbar-link")
        dropbox = navbar[8]
        dropbox.click()

        # Selects the current lab that will be graded.
        lab_number = input("what lab number is this?: ")
        lab = self.browser.find_element_by_link_text('Lab '+lab_number)
        lab.click()




