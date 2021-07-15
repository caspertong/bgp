import time
from attr import s
import pytest

import preparation
from Pages import summary, business_impact, grant
from Pages.utils import read_all_test_data, get_testcase_test_data

#User Story #3
#AC1 and AC3
#This TC will pass
def test_fill_up_all_forms(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    preparation.run_eligibility(driver)
    time.sleep(1)
    preparation.run_contact_details(driver)
    time.sleep(1)
    preparation.run_proposal(driver)
    time.sleep(1)
    preparation.run_business_impact(driver)
    time.sleep(1)
    preparation.run_cost(driver)
    time.sleep(1)
    preparation.run_declaration(driver)
    time.sleep(2)
    #AC1 Verify Summary Page showed and Read Only
    summary.verify_summary_page(driver)
    summary.verify_read_only(driver)
    #AC3 Verify all the input showed correctly in Summary Page
    #Form 1
    summary.verify_eligibility(driver)
    #Form 2
    summary.verify_main_contact(driver, 'Tan Ah Kow', 'IT', '98765432', 'ahkow@testmail.com', 'nil')
    summary.verify_main_address(driver, '320 BUKIT BATOK STREET 33,', '#03-33,', 'SINGAPORE 650320')
    summary.verify_letter_offer(driver, 'Tan Ah Kow', 'IT','ahkow@testmail.com')
    #Form 3
    summary.verify_proposal_field(driver, 'Test Project', '01 Aug 2021', '01 Oct 2021', 'Test Description')
    summary.verify_proposal_activity(driver, 'Market Entry', 'nil', '0.00%')
    summary.verify_proposal_market(driver, 'China', 'Yes', 'nil', 'nil')
    #Form 4
    summary.verify_business_fy(driver, '31 Mar 2021', '31 Mar 2022', '31 Mar 2023', '31 Mar 2024')
    summary.verify_business_sales(driver, '100,000.00', '100,000.00', '100,000.00', '100,000.00')
    summary.verify_business_investment(driver, '1,000,000.00', '1,000,000.00', '1,000,000.00', '1,000,000.00')
    summary.verify_business_activity(driver, 'Test Rationale', 'Test Benefit')
    #Form 5
    summary.verify_cost(driver, 'Overseas', 'Test Vendor', 'dummy.pdf', 'SGD 2,000,000.00', 'nil')
    #Form 6
    summary.verify_declare(driver, 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'Yes')
    return

#AC2
#This TC will pass
def test_missing_mandatory(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    preparation.run_eligibility(driver)
    time.sleep(1)
    preparation.run_contact_details(driver)
    time.sleep(1)
    preparation.run_proposal(driver)
    time.sleep(1)
    business_impact.input_fy_end_date(driver, '31 Mar 2021')
    business_impact.input_proposal_field(driver, '100000', '1000000')
    business_impact.click_next_btn(driver)
    time.sleep(1)
    preparation.run_cost(driver)
    time.sleep(1)
    preparation.run_declaration(driver)
    time.sleep(2)
    business_impact.verify_section_tab_active(driver)
    summary.verify_missing_field_num(driver, '2')
    #Verify the alert and the alert color
    business_impact.verify_field_alert(driver, "rgba(255, 89, 97, 1)")
    return

#AC4, #AC5 and #AC6
#This TC will pass
def test_ack_submit(get_driver_webdriver):
    driver = get_driver_webdriver
    preparation.run_login(driver)
    preparation.run_new_grant(driver)

    time.sleep(1)
    preparation.run_eligibility(driver)
    time.sleep(1)
    preparation.run_contact_details(driver)
    time.sleep(1)
    preparation.run_proposal(driver)
    time.sleep(1)
    preparation.run_business_impact(driver)
    time.sleep(1)
    preparation.run_cost(driver)
    time.sleep(1)
    preparation.run_declaration(driver)
    time.sleep(2)
    #AC4 Click Declare
    summary.click_declare_check(driver)
    summary.click_submit_btn(driver)
    time.sleep(1)
    #AC5 Verify Ref ID and Agency Details
    refid = summary.verify_ref_id_contains_value(driver)
    summary.verify_agency_details(driver, 'Enterprise Singapore')
    #AC6 Verify Grant Listed in Processing
    status = summary.get_status(driver)
    date = summary.get_submit_date(driver)
    grant.click_my_grant_tab(driver)
    time.sleep(2)
    grant.click_applications_tab(driver)
    grant.click_processing_tab(driver)
    grant.verify_ref_id(driver, refid)
    time.sleep(1)
    grant.verify_agency(driver, refid, 'Enterprise Singapore')
    grant.verify_project_title(driver, refid, 'Test Project')
    grant.verify_status(driver, refid, status)
    grant.verify_submitted_date(driver, refid, date)
    return