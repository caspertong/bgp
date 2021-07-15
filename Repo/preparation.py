import time
import pytest
import os

from Pages import login, new_grant, eligibility, contact_details, proposal, business_impact, cost, declaration
from Pages.utils import random_mobile, random_name, random_email

def run_login(driver):
    time.sleep(2)

    login.click_login_btn(driver)
    login.input_nric(driver, 'S1234567A')
    login.input_name(driver, 'Tan Ah Kow')
    login.input_uen(driver, 'BGPQEDEMO')
    login.input_dropdown_role(driver, 'Acceptor')
    login.click_login_login_btn(driver)

    time.sleep(2)
    login.verify_username(driver, 'Tan Ah Kow')
    login.verify_role(driver, 'Acceptor')
    time.sleep(5)

def run_new_grant(driver):
    new_grant.click_get_new_grant_btn(driver)
    new_grant.click_business_btn(driver, 'IT')
    new_grant.click_purpose_btn(driver, 'International Expansion')
    new_grant.click_business_plan(driver, 'Market Readiness Assistance 2')
    time.sleep(1)
    new_grant.click_apply_btn(driver)
    time.sleep(1)
    new_grant.click_proceed_btn(driver)

def run_eligibility(driver):
    eligibility.select_all_qns_yes(driver)
    time.sleep(1)
    eligibility.click_next_btn(driver)

def run_contact_details(driver):
    contact_details.input_contact_detail(driver, "Tan Ah Kow", 'IT', "98765432", "ahkow@testmail.com")
    contact_details.click_same_registered_address(driver)
    contact_details.click_same_main_person(driver)
    contact_details.click_next_btn(driver)

def run_proposal(driver):
    proposal.input_proposal_field(driver, "Test Project", "01 Aug 2021", "01 Oct 2021", "Test Description")
    proposal.input_activity(driver, "Market Entry")
    proposal.input_target_market(driver, "China")
    proposal.select_expand_outside(driver, 'Yes')
    proposal.click_next_btn(driver)

def run_business_impact(driver):
    business_impact.input_fy_end_date(driver, "31 Mar 2021")
    business_impact.input_proposal_field(driver, "100000", "1000000")
    business_impact.input_activity(driver, "Test Rationale", "Test Benefit")
    business_impact.click_next_btn(driver)

def run_cost(driver):
    cost.click_add_third_vendor(driver)
    time.sleep(1)
    cost.click_oversea_vendor(driver)
    cost.input_vendor_name(driver, "Test Vendor")
    pdfpath = os.path.abspath("dummy.pdf")
    cost.input_vendor_attachment(driver, pdfpath)
    time.sleep(1)
    cost.input_vendor_cost(driver, "2000000")
    cost.click_next_btn(driver)

def run_declaration(driver):
    declaration.map_all_ans(driver, "No", "No", "No", "No", "No", "No", "No", "No", "Yes", "Yes")
    declaration.click_consent_check(driver)
    declaration.click_review_btn(driver)