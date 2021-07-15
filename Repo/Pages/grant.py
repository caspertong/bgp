import time
import pytest

from Pages import utils

def click_my_grant_tab(driver):
    utils.click_btn(driver, "My Grants Section Tab", "//a[@alt='Dashboard']")

def click_applications_tab(driver):
    utils.click_btn(driver, "Application Tab", "//a[text()='Applications']")

def click_processing_tab(driver):
    utils.click_btn(driver, "Processing Tab", "//a[@href='#processing']")

def verify_ref_id(driver, ref):
    utils.verify_element_exist(driver, "Ref ID", "//td[text()='"+ref+"']")

def verify_agency(driver, ref, agency):
    utils.verify_text(driver, "Agency", "//td[text()='"+ref+"']/following-sibling::*[2]", agency)

def verify_project_title(driver, ref, title):
    utils.verify_text(driver, "Project title", "//td[text()='"+ref+"']/following-sibling::*[3]", title)

def verify_status(driver, ref, status):
    utils.verify_text(driver, "Status", "//td[text()='"+ref+"']/following-sibling::*[4]", status)

def verify_submitted_date(driver, ref, date):
    utils.verify_text(driver, "Submitted Date", "//td[text()='"+ref+"']/following-sibling::*[5]", date)