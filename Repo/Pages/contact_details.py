import time
import pytest

from Pages import utils

from selenium.webdriver.common.keys import Keys

def verify_main_contact_input(driver):
    utils.verify_text(driver, "Name Input", "//label[@id='react-contact_info-name-label']", "Name *")
    utils.verify_text(driver, "Job Title Input", "//label[@id='react-contact_info-designation-label']", "Job Title *")
    utils.verify_text(driver, "Contact Input", "//label[@id='react-contact_info-phone-label']", "Contact No. *")
    utils.verify_text(driver, "Email Input", "//label[@id='react-contact_info-primary_email-label']", "Email *")
    utils.verify_text(driver, "Email Input", "//label[@id='react-contact_info-secondary_email-label']", "Alternate Contact Person's Email")
    try:
        el = driver.find_element_by_xpath("//label[text()='Mailing Address']")
        if el:
            print("Verify Mailing Address Successful")
        else:
            pytest.fail("Mailing Address Input not found")
    except Exception:
        pytest.fail("Failed to verify Mailing Address")

def input_contact_detail(driver, name, job, contact, email):
    utils.input_text_without_clear(driver, "Name", "//input[@id='react-contact_info-name']", name)
    utils.input_text_without_clear(driver, "Job", "//input[@id='react-contact_info-designation']", job)
    utils.input_text_without_clear(driver, "Contact", "//input[@id='react-contact_info-phone']", contact)
    utils.input_text_without_clear(driver, "Email", "//input[@id='react-contact_info-primary_email']", email)

def input_postal_code(driver, postal):
    utils.input_text_without_clear(driver, "Postal Code", "//input[@id='react-contact_info-correspondence_address-postal']", postal)
    utils.click_btn(driver, "Search Postal","//span[@id='react-contact_info-correspondence_address-postal-postal']")

def click_same_registered_address(driver):
    utils.click_btn(driver, "Same as Registered Address", "//input[@id='react-contact_info-correspondence_address-copied']")

def click_same_main_person(driver):
    utils.click_btn(driver, "Same as Main Person", "//input[@id='react-contact_info-copied']")

def click_save_btn(driver):
    utils.click_btn(driver, "Save Btn", "//button[@id='save-btn']")

def click_next_btn(driver):
    utils.click_btn(driver, "Next Btn", "//button[@id='next-btn']")

def verify_block_street(driver, block, street):
    utils.verify_value(driver, "Block Number", "//input[@id='react-contact_info-correspondence_address-block']", block)
    utils.verify_value(driver, "Street Name", "//input[@id='react-contact_info-correspondence_address-street']", street)

def verify_postal_code(driver, postal):
    utils.verify_value(driver, "Postal Code", "//input[@id='react-contact_info-correspondence_address-postal']", postal)

def verify_level_unit(driver, level, unit):
    utils.verify_value(driver, "Level", "//input[@id='react-contact_info-correspondence_address-level']", level)
    utils.verify_value(driver, "Unit", "//input[@id='react-contact_info-correspondence_address-unit']", unit)

def verify_letter_offer_input(driver):
    utils.verify_text(driver, "Name", "//label[@id='react-contact_info-offeree_name-label']", "Name *")
    utils.verify_text(driver, "Job Title", "//label[@id='react-contact_info-offeree_designation-label']", "Job Title *")
    utils.verify_text(driver, "Email", "//label[@id='react-contact_info-offeree_email-label']", "Email *")

def verify_letter_offer_input_text(driver, name, job, email):
    utils.verify_value(driver, "Name Input", "//input[@id='react-contact_info-offeree_name']", name)
    utils.verify_value(driver, "Job Title Input", "//input[@id='react-contact_info-offeree_designation']", job)
    utils.verify_value(driver, "Email Input", "//input[@id='react-contact_info-offeree_email']", email)

def verify_main_contact_input_text(driver, name, job, contact, email):
    utils.verify_value(driver, "Name Input", "//input[@id='react-contact_info-name']", name)
    utils.verify_value(driver, "Job Title Input", "//input[@id='react-contact_info-designation']", job)
    utils.verify_value(driver, "Contact Input", "//input[@id='react-contact_info-phone']", contact)
    utils.verify_value(driver, "Email Input", "//input[@id='react-contact_info-primary_email']", email)


def input_contact_name_clear(driver, name):
    utils.input_text_without_clear(driver, "Name", "//input[@id='react-contact_info-name']", name)
    try: 
        el = driver.find_element_by_xpath("//input[@id='react-contact_info-name']")
        for i in range (len(el.get_attribute("value"))):
            el.send_keys(Keys.BACKSPACE)
        el_other = driver.find_element_by_xpath("//label[@id='react-contact_info-name-label']")
        el_other.click()
        print("Input Name then clear successful")
    except Exception:
        pytest.fail("Failed to Input and clear Name")

def verify_input_name_alert(driver, colour):
    utils.verify_text(driver, "Name Input Alert", "//p[@id='react-contact_info-name-alert']", "We need a response for this field")
    try:
        el = driver.find_element_by_xpath("//p[@id='react-contact_info-name-alert']")
        el_color = el.value_of_css_property("color")
        if el_color == colour:
            print("Color Red of the alert matched.")
        else:
            pytest.fail("Color is not matched. Expected: "+colour+" Actual: "+el_color)
    except Exception:
        pytest.fail("Failed to verify color alert")