import time
import pytest

from Pages import utils

def click_get_new_grant_btn(driver):
    utils.click_btn(driver, "Get New Grant", "//a[@id='dashboard-menubox-app-apply-grant']//div[@class='dashboard-action-card']")

def click_business_btn(driver, bus):
    utils.click_form_btn(driver, "Business Sector", bus)

def click_purpose_btn(driver, pur):
    utils.click_form_btn(driver, "Gant Purpose", pur)

def click_business_plan(driver, plan):
    utils.click_form_btn(driver, "Business Plan", plan)

def click_apply_btn(driver):
    utils.click_btn(driver, "Apply Button", "//button[@id='go-to-grant']")

def click_proceed_btn(driver):
    utils.click_btn(driver, "Proceed Button", "//button[@id='keyPage-form-button']")