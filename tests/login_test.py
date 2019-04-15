from selenium import webdriver
import pytest
import allure
import moment
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():


    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            home = HomePage(driver)
            home.click_welcome()
            home.click_logout()
            x = driver.title
            assert x == "abc"
        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currTime = moment.now().strftime("%Y-%m-%d - %H:%M:%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/AutomationFramework/screenshots/" + screenshotName +".png")
            raise
        except:
            print("There was an exception")
            raise
        else:
            print("No exceptions occurred")
        finally:
            print("I am inside finally block")
