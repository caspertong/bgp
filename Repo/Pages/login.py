import time
import pytest

from Pages import utils

def click_login_btn(driver):
    utils.click_btn(driver, "Login", "//a[@id='login-button']")

def input_nric(driver, nric):
    utils.input_text(driver, "NIRC", "//input[@name='CPUID']", nric)

def input_name(driver, name):
    utils.input_text(driver, "Name", "//input[@name='CPUID_FullName']", name)

def input_uen(driver, uen):
    utils.input_text(driver, "UEN", "//input[@name='CPEntID']", uen)

def input_dropdown_role(driver, role):
    try:
        el = driver.find_element_by_xpath("//select[@name='CPRole']")
        utils.scroll_to_element(driver, el)
        option = el.find_element_by_xpath("//option[@value='"+role+"']")
        option.click()
        print("Input Role Successful")
    except Exception:
        pytest.fail("Failed to Input Role") 

def click_login_login_btn(driver):
    try:
        el = driver.find_elements_by_xpath("//button[@type='submit']")
        utils.scroll_to_element(driver, el[1])
        el[1].click()
        print("Click on Login Page Login Btn Successful")
    except Exception:
        pytest.fail("Failed to click on Login Page Login Btn")

def verify_username(driver, username):
    try:
        el = driver.find_elements_by_xpath("//div[@class='username']")
        utils.scroll_to_element(driver, el[1])
        if el[1].text == username:
            print("Verified Username displayed is Correct")
        else:
            pytest.fail("Username displayed is incorrect. Actual: "+el[1].text+" Expected: "+username)
    except Exception:
        pytest.fail("Failed to verify Username")


def verify_role(driver, role):
    try:
        el = driver.find_element_by_xpath("//a[text()='"+role+"']")
        utils.scroll_to_element(driver, el)
        if el:
            print("Verified Role displayed correctly")
        else:
            pytest.fail("Role displayed is incorrect.")
    except Exception:
        pytest.fail("Failed to verify role")