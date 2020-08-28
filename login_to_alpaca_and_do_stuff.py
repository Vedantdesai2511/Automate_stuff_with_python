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

    driver.close()


print(open_browser())
