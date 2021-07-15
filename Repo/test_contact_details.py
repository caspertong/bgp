import time
import pytest

import preparation
from Pages import contact_details
from Pages.utils import read_all_test_data, get_testcase_test_data

#User Story #2
#AC1
#This TC will pass
def test_contact_main_contact(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    preparation.run_eligibility(driver)
    time.sleep(1)
    contact_details.verify_main_contact_input(driver)
    return

#AC2
#This TC will pass
def test_contact_postal(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    preparation.run_eligibility(driver)
    time.sleep(1)
    contact_details.input_postal_code(driver, "408724")
    time.sleep(2)
    contact_details.verify_block_street(driver, "21", "UBI ROAD 1")
    return

#AC3
#This TC will pass
def test_contact_same_address(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    preparation.run_eligibility(driver)
    time.sleep(1)
    contact_details.click_same_registered_address(driver)
    time.sleep(2)
    contact_details.verify_postal_code(driver, "650320")
    contact_details.verify_block_street(driver, "320", "BUKIT BATOK STREET 33")
    contact_details.verify_level_unit(driver, "03", "33")
    return

#AC4
#This TC will pass
def test_contact_letter_offer_input(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    preparation.run_eligibility(driver)
    time.sleep(1)
    contact_details.verify_letter_offer_input(driver)
    return

#AC5
#This TC will pass
def test_contact_letter_offer_same_main(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    preparation.run_eligibility(driver)
    time.sleep(1)
    contact_details.input_contact_detail(driver, "Tan Ah Kow", "IT", "92840184", "tanakkow@gmail.com")
    contact_details.click_same_main_person(driver)
    time.sleep(2)
    contact_details.verify_letter_offer_input_text(driver, "Tan Ah Kow", "IT", "tanakkow@gmail.com")
    return

#AC6
#This TC will pass
def test_contact_input_save(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    preparation.run_eligibility(driver)
    time.sleep(1)
    contact_details.input_contact_detail(driver, "Tan Ah Kow", "IT", "92840184", "tanakkow@gmail.com")
    contact_details.click_same_registered_address(driver)
    contact_details.click_same_main_person(driver)
    contact_details.click_save_btn(driver)
    time.sleep(2)
    driver.refresh()
    time.sleep(1)
    contact_details.verify_main_contact_input_text(driver, "Tan Ah Kow", "IT", "92840184", "tanakkow@gmail.com")
    contact_details.verify_postal_code(driver, "650320")
    contact_details.verify_block_street(driver, "320", "BUKIT BATOK STREET 33")
    contact_details.verify_level_unit(driver, "03", "33")
    contact_details.verify_letter_offer_input_text(driver, "Tan Ah Kow", "IT", "tanakkow@gmail.com")
    return

#Additional Test Case
#Verify if cleared an Mandatory Field and did not filled in
def test_empty_field_after_clear(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    preparation.run_eligibility(driver)
    time.sleep(1)

    contact_details.input_contact_name_clear(driver, "Tan Ah Kow")
    contact_details.verify_input_name_alert(driver, "rgba(255, 89, 97, 1)")
    return