import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

__author__ = 'Phil'
from selenium import webdriver

def pushGrades(gradeFile):
    """
    reads in all grades from a text file and places them
    in the grade box on mycourses
    """
    # Initialize the empty list to hold grades from the file
    # Append the grades to the list.
    grades = []
    for line in gradeFile:
        grades.append(line.strip())

    # Open Firefox
    d = webdriver.Firefox()

    # Go to mycourses
    d.get("https://mycourses.rit.edu")

    # TODO: *** make selenium navigate to the proper lab grading page and replace this input ***
    input("Please navigate to Lab page then press enter.")

    # find all the textboxes
    #grade_boxes = d.find_elements_by_css_selector("input.d_edt")
    grade_boxes = d.find_elements_by_css_selector("input.d_edt")[3:]
    for i in range(0,len(grades)):
        # send keys to each text box
        grade_boxes[i].send_keys(grades[i])
        # the grade box starts at index 3 so add 3
        #grade_boxes[i+3].send_keys(grades[i])
    return d

def gradingRubric(driver,rubricFile):
    """
    push the grading rubric into the feedback textbox.

    driver - the webdriver used to send the grades
    rubricFile - an opened file containing the grading rubric
    :return:
    """

    # string slicing to follow feedback button pattern
    feedback_buttons = driver.find_elements_by_css_selector("a.di_l.vui-outline")[3:53:2]

    # store text in the text file
    rubric = rubricFile.readlines()

    wait = WebDriverWait(driver, 10)
    # for i in range(3,len(feedback_buttons)-3):
        # if i % 2 == 0:
            #pass
        # else:

    for i in range( 0, len( feedback_buttons )):
        # click the feedback buttons
        feedback_buttons[i].click()

        # switch to the feedback overall iframe
        feedback_frame = driver.find_elements_by_tag_name("iframe")[1]
        driver.switch_to.frame(feedback_frame)

        # wait until student frame loads and when it does switch to that iframe
        # once in that iframe, send feedback
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="publicComments$html_ifr"]')))
        feedback = driver.find_element_by_xpath('//*[@id="tinymce"]')
        feedback.click()
        feedback.send_keys(rubric)

        # switch back to default content and click the save button.
        driver.switch_to.default_content()
        save_feedback = driver.find_element_by_xpath('//*[@id="d2l_body"]/div[9]/div/div[1]/table/tbody/tr/td[1]/a[1]')
        save_feedback.click()



def main():

    gFile = open("grades.txt")
    driver = pushGrades(gFile)
    #rFile = open("rubric.txt")
    #gradingRubric(driver,rFile)
    gFile.close()
    #rFile.close()

main()
