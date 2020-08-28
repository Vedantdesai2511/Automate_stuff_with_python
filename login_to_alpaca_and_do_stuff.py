from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
from selenium.webdriver.common.keys import Keys

# This code is for opening the alpaca web interface while the algorithm is running


def open_browser():
    driver = webdriver.Chrome("chromedriver.exe")  # open google chrome using chrome driver
    a = driver.get("https://alpaca.markets/")  # Open the alpaca url using the chrome driver

    time.sleep(0.5)  # the sleep comment is to give the chrome driver time to open the page and load all the elements
    # on the page

    print(a)

    driver.find_elements_by_class_name("menu__link")[5].click()  # select the log in button on the page and click on
    # it, Since log in button the page does not have id here I have used class name to select the element

    time.sleep(1)  # The program just clicked on the login page so this sleep command is t give the webpage time to
    # redirect it to the login page

    driver.find_elements_by_id("username")[0].click()  # Select the username text-box and click on it

    e = driver.find_elements_by_id("username")[0]  # store the username element is a variable

    e.send_keys("vedantdesai07@gmail.com")  # Type in the email address

    driver.find_elements_by_id("password")[0].click()  # Select the password text-box and click on it

    e = driver.find_elements_by_id("password")[0]  # store the password element is a variable

    e.send_keys("Vedantdesai@25111996")  # Type in the password
    e.send_keys(Keys.RETURN)  # Press enter

    time.sleep(2.5)  # wait for the webpage to redirect to the next page

    driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "fa-flask", " " ))]').click()
    # select the "papper trading" element by x-path and click on it

    e = driver.find_elements_by_xpath('rheyrhtv').click()  # crash the program so that the chrome window does not
    # close after the program is done executing
    print(e)

    driver.close()


print(open_browser())
