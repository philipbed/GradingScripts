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


class Download:

    def __init__( self, driver=webdriver.Firefox()):
        self.browser = driver
        self.url = driver.current_url
        self.browser.implicitly_wait(10)

    def open( self, link ):
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

        def navigate_to_lab(self):
            flyout = self.browser.find_element_by_css_selector("a.d2l-menuflyout-opener.d2l-clickable")
            flyout.click()

            computer_science_one = self.browser.find_element_by_partial_link_text("Computer Science I")
            computer_science_one.click()

            navbar = self.browser.find_elements_by_css_selector("a.d2l-navbar-link")
            dropbox = navbar[8]

            dropbox.click()
            lab = self.browser.find_element_by_link_text('Lab 1')
            lab.click()


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
        frames = self.browser.find_elements_by_tag_name('frame')

        frame = frames[1]
        self.browser.switch_to.frame(frame)
        download = self.browser.find_element_by_css_selector('span.dfl>a')
        download.click()


    def navigate_to_lab(self):
        flyout = self.browser.find_element_by_css_selector("a.d2l-menuflyout-opener.d2l-clickable")
        flyout.click()

        computer_science_one = self.browser.find_element_by_partial_link_text("Computer Science I")
        computer_science_one.click()

        navbar = self.browser.find_elements_by_css_selector("a.d2l-navbar-link")
        dropbox = navbar[8]

        dropbox.click()
        lab_number = input("what lab number is this?: ")
        lab = self.browser.find_element_by_link_text('Lab '+lab_number)
        lab.click()




if __name__ == '__main__':

    d = Download()
    go_to = 'https://mycourses.rit.edu'
    d.open(go_to)
    d.login()
    d.navigate_to_lab()
    d.select_all()
    d.change_windows()
    d.download_all()

