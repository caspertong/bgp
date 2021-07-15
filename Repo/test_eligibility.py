import time
import pytest

import preparation
from Pages import eligibility
from Pages.utils import read_all_test_data, get_testcase_test_data

#User Story #1
#AC1
#This TC will fail, because there is 5 questions instead of 4 in Eligibility Form
def test_eligibility_question(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    eligibility.verify_qn1_text(driver)
    eligibility.verify_qn2_text(driver)
    eligibility.verify_qn3_text(driver)
    eligibility.verify_qn5_text(driver)
    eligibility.verify_total_qns(driver)
    return

#AC2
#This TC will return a pass
def test_eligibility_selection(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    eligibility.verify_qn1_type(driver)
    eligibility.verify_qn2_type(driver)
    eligibility.verify_qn3_type(driver)
    eligibility.verify_qn4_type(driver)
    eligibility.verify_qn5_type(driver)
    return

#AC3
#This TC will return fail, because the warning message is different
def test_eligibility_select_no_msg(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    eligibility.answer_qn1_no(driver)
    eligibility.verify_warning_msg(driver)
    return

#AC4
#This TC will return fail, because the warning message url is different
def test_eligibility_select_no_url(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    eligibility.answer_qn1_no(driver)
    eligibility.verify_warning_url(driver)
    return

#AC5
#This TC will return pass
def test_eligibility_save_refresh(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    eligibility.select_all_qns_yes(driver)
    time.sleep(1)
    eligibility.click_save_btn(driver)
    time.sleep(2)
    driver.refresh()
    time.sleep(1)
    eligibility.verify_selection_saved(driver)
    return