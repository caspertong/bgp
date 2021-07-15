import time
import pytest

from Pages import utils

def input_proposal_field(driver, title, startdate, enddate, desc):
    utils.input_text_without_clear(driver, "Project Title", "//input[@id='react-project-title']", title)
    utils.input_text_without_clear(driver, "Start Date", "//input[@id='react-project-start_date']", startdate)
    utils.input_text_without_clear(driver, "End Date", "//input[@id='react-project-end_date']", enddate)
    utils.input_text_without_clear(driver, "Project Description", "//textarea[@id='react-project-description']", desc)

def input_activity(driver, activity):
    try:
        el = driver.find_element_by_xpath("//span[@id='react-select-project-activity--value']")
        utils.scroll_to_element(driver, el)
        el.click()
        el_select = driver.find_element_by_xpath("//*[text()='"+activity+"']")
        el_select.click()
        print("Select Activity "+activity+" Successful")
    except Exception:
        pytest.fail("Failed to select "+activity)

def input_target_market(driver, market):
    try:
        el = driver.find_element_by_xpath("//span[@id='react-select-project-primary_market--value']")
        utils.scroll_to_element(driver, el)
        el.click()
        el_select = driver.find_element_by_xpath("//*[text()='"+market+"']")
        utils.scroll_to_element(driver, el_select)
        el_select.click()
        print("Select Activity "+market+" Successful")
    except Exception:
        pytest.fail("Failed to select "+market)

def select_expand_outside(driver, ans):
    if ans == 'Yes':
        select = 'true'
    else:
        select = 'false'
    utils.click_btn(driver, "Outside Singapore "+ans, "//input[@id='react-project-is_first_time_expand-"+select+"']")

def click_save_btn(driver):
    utils.click_btn(driver, "Save Btn", "//button[@id='save-btn']")

def click_next_btn(driver):
    utils.click_btn(driver, "Next Btn", "//button[@id='next-btn']")