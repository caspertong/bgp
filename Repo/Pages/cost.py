import time
import pytest

from Pages import utils

def click_add_third_vendor(driver):
    utils.click_btn(driver, "Third Party Vendors", "//div[@id='react-project_cost-vendors-accordion-header']")
    utils.click_btn(driver, "Third Party Vendors Add", "//button[@id='react-project_cost-vendors-add-item']")

def click_add_office_rental(driver):
    utils.click_btn(driver, "Third Party Vendors", "//div[@id='react-project_cost-office_rentals-accordion-header']")
    utils.click_btn(driver, "Third Party Vendors Add", "//button[@id='react-project_cost-office_rentals-add-item']")

def click_add_salary(driver):
    utils.click_btn(driver, "Third Party Vendors", "//div[@id='react-project_cost-salaries-accordion-header']")
    utils.click_btn(driver, "Third Party Vendors Add", "//button[@id='react-project_cost-salaries-add-item']")

def click_oversea_vendor(driver):
    utils.click_btn(driver, "Overseas Vendor", "//input[@id='react-project_cost-vendors-0-local_vendor-false']")


def input_vendor_name(driver, vendor):
    utils.input_text_without_clear(driver, "Vendor Name", "//input[@id='react-project_cost-vendors-0-vendor_name']", vendor)


def input_vendor_attachment(driver, attachment):
    utils.input_text_without_clear(driver, "Vendor Attachment", "//input[@id='react-project_cost-vendors-0-attachments-input']", attachment)

def input_vendor_cost(driver, cost):
    utils.input_text_without_clear(driver, "Vendor Cost", "//input[@id='react-project_cost-vendors-0-amount_in_billing_currency']", cost)

def click_save_btn(driver):
    utils.click_btn(driver, "Save Btn", "//button[@id='save-btn']")

def click_next_btn(driver):
    utils.click_btn(driver, "Next Btn", "//button[@id='next-btn']")