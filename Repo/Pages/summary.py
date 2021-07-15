import time
import pytest

from datetime import datetime
from Pages import utils

def verify_summary_page(driver):
    utils.wait_until_xpath(driver, "//div[@class='main summary-page']", 20)
    utils.verify_element_exist(driver, "Summary Page", "//div[@class='main summary-page']")

def verify_read_only(driver):
    try:
        el = driver.find_elements_by_xpath("//input")
        if len(el) > 3:
            pytest.fail("Multiples input available in Summary Page")
        else:
            el_1 = driver.find_element_by_xpath("//input[@id='search-box-mobile']")
            el_2 = driver.find_element_by_xpath("//input[@id='search-box-desktop']")
            el_3 = driver.find_element_by_xpath("//input[@id='react-declaration-info_truthfulness_check']")
            if el_1 and el_2 and el_3:
                print("All input are not to edit the field")
            else:
                pytest.fail("1 or more input are unknown")
    except Exception:
        pytest.fail("Failed to verify read only")

def verify_eligibility(driver):
    utils.verify_text(driver, "Question1 Yes Radio", "//div[@id='react-eligibility-sg_registered_check']", "Yes")
    utils.verify_text(driver, "Question2 Yes Radio", "//div[@id='react-eligibility-turnover_check']", "Yes")
    utils.verify_text(driver, "Question3 Yes Radio", "//div[@id='react-eligibility-global_hq_check']", "Yes")
    utils.verify_text(driver, "Question4 Yes Radio", "//div[@id='react-eligibility-new_target_market_check']", "Yes")
    utils.verify_text(driver, "Question5 Yes Radio", "//div[@id='react-eligibility-started_project_check']", "Yes")

def verify_main_contact(driver, name, job, contact, email, alt_email):
    utils.verify_text(driver, "Name", "//div[@id='react-contact_info-name']", name)
    utils.verify_text(driver, "Job", "//div[@id='react-contact_info-designation']", job)
    utils.verify_text(driver, "Contact", "//div[@id='react-contact_info-phone']", contact)
    utils.verify_text(driver, "Email", "//div[@id='react-contact_info-primary_email']", email)
    utils.verify_text(driver, "Alternate Email", "//div[@id='react-contact_info-secondary_email']", alt_email)

def verify_main_address(driver, add1, add2, add3):
    try:
        el = driver.find_element_by_xpath("//div[@id='react-contact_info-correspondence_address']")
        utils.scroll_to_element(driver, el)
        if add1 in el.text:
            print("Block and Street Name verified")
            if add2 in el.text:
                print("Unit and Level verified")
                if add3 in el.text:
                    print("Postal Code verified")
                else:
                    pytest.fail("Postal Code incorrect")
            else:
                pytest.fail("Unit or Level incorrect")
        else:
            pytest.fail("Block or Street Name incorrect")
    except Exception:
        pytest.fail("Failed to verify Main Address")

def verify_letter_offer(driver, name, job, email):
    utils.verify_text(driver, "Name", "//div[@id='react-contact_info-offeree_name']", name)
    utils.verify_text(driver, "Job Title", "//div[@id='react-contact_info-offeree_designation']", job)
    utils.verify_text(driver, "Email", "//div[@id='react-contact_info-offeree_email']", email)

def verify_proposal_field(driver, title, startdate, enddate, desc):
    utils.verify_text(driver, "Project Title", "//div[@id='react-project-title']", title)
    utils.verify_text(driver, "Start Date", "//div[@id='react-project-start_date']", startdate)
    utils.verify_text(driver, "End Date", "//div[@id='react-project-end_date']", enddate)
    utils.verify_text(driver, "Project Description", "//div[@id='react-project-description']", desc)

def verify_proposal_activity(driver, activity, entity, percentage):
    utils.verify_text(driver, "Activity", "//div[@id='react-project-activity']", activity)
    utils.verify_text(driver, "Type of Entity", "//div[@id='react-project-entity_type']", entity)
    utils.verify_text(driver, "Activity", "//div[@id='react-project-shareholding_percentage']", percentage)

def verify_proposal_market(driver, market, first, doc, remark):
    utils.verify_text(driver, "Primary market", "//div[@id='react-project-primary_market']", market)
    utils.verify_text(driver, "First Time Expand", "//div[@id='react-project-is_first_time_expand']", first)
    utils.verify_text(driver, "Supporting Document", "//label[text()='Any other Supporting Documents']/../following-sibling::*[1]/div/span", doc)
    utils.verify_text(driver, "Market Remarks", "//div[@id='react-project-remarks']/span", remark)

def verify_business_fy(driver, year1, year2, year3, year4):
    utils.verify_text(driver, "Current FY End Date", "//div[@id='react-project_impact-fy_end_date_0']", year1)
    utils.verify_text(driver, "Next FY End Date", "//div[@id='react-project_impact-fy_end_date_1']", year2)
    utils.verify_text(driver, "Next Next FY End Date", "//div[@id='react-project_impact-fy_end_date_2']", year3)
    utils.verify_text(driver, "Next Next Next FY End Date", "//div[@id='react-project_impact-fy_end_date_3']", year4)

def verify_business_sales(driver, sales1, sales2, sales3, sales4):
    utils.verify_text(driver, "Current FY Sales", "//div[@id='react-project_impact-overseas_sales_0']", sales1)
    utils.verify_text(driver, "Next FY Sales", "//div[@id='react-project_impact-overseas_sales_1']", sales2)
    utils.verify_text(driver, "Next Next FY Sales", "//div[@id='react-project_impact-overseas_sales_2']", sales3)
    utils.verify_text(driver, "Next Next Next FY Sales", "//div[@id='react-project_impact-overseas_sales_3']", sales4)

def verify_business_investment(driver, invest1, invest2, invest3, invest4):
    utils.verify_text(driver, "Current FY Investment", "//div[@id='react-project_impact-overseas_investments_0']", invest1)
    utils.verify_text(driver, "Next FY Investment", "//div[@id='react-project_impact-overseas_investments_1']", invest2)
    utils.verify_text(driver, "Next Next FY Investment", "//div[@id='react-project_impact-overseas_investments_2']", invest3)
    utils.verify_text(driver, "Next Next Next FY Investment", "//div[@id='react-project_impact-overseas_investments_3']", invest4)

def verify_business_activity(driver, rational, nontangible):
    utils.verify_text(driver, "Rational for Projections", "//div[@id='react-project_impact-rationale_remarks']", rational)
    utils.verify_text(driver, "Non Tangible Benefits", "//div[@id='react-project_impact-benefits_remarks']", nontangible)

def verify_cost(driver, oversea, vendor, pdf, cost, remark):
    utils.verify_text(driver, "Vendor Overseas", "//div[@id='react-project_cost-vendors-0-local_vendor']", oversea)
    utils.verify_text(driver, "Vendor Name", "//div[@id='react-project_cost-vendors-0-vendor_name']", vendor)
    utils.verify_element_exist(driver, "Upload File", "//a[text()='"+pdf+"']")
    utils.verify_text(driver, "Estimated Cost Billing", "//div[@id='react-project_cost-vendors-0-amount_in_billing_currency']", cost)
    utils.verify_text(driver, "Estimated Cost", "//div[@id='react-project_cost-vendors-0-estimated_cost']", cost)
    utils.verify_text(driver, "Cost Remark", "//div[@id='react-project_cost-vendors-0-remarks']/span", remark)

def verify_declare(driver, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
    utils.verify_text(driver, "Question 1", "//div[@id='react-declaration-criminal_liability_check']", ans1)
    utils.verify_text(driver, "Question 2", "//div[@id='react-declaration-civil_proceeding_check']", ans2)
    utils.verify_text(driver, "Question 3", "//div[@id='react-declaration-insolvency_proceeding_check']", ans3)
    utils.verify_text(driver, "Question 4", "//div[@id='react-declaration-project_incentives_check']", ans4)
    utils.verify_text(driver, "Question 5", "//div[@id='react-declaration-other_incentives_check']", ans5)
    utils.verify_text(driver, "Question 6", "//div[@id='react-declaration-project_commence_check']", ans6)
    utils.verify_text(driver, "Question 7", "//div[@id='react-declaration-related_party_check']", ans7)
    utils.verify_text(driver, "Question 8", "//div[@id='react-declaration-debarment_check']", ans8)
    utils.verify_text(driver, "Question 9", "//div[@id='react-declaration-covid_safe_check']", ans9)
    utils.verify_text(driver, "Question 10", "//div[@id='react-declaration-covid_safe_ques_check']", ans10)

def click_declare_check(driver):
    utils.click_btn(driver, "Declare Check Box", "//input[@id='react-declaration-info_truthfulness_check']")

def click_submit_btn(driver):
    utils.click_btn(driver, "Save Btn", "//button[@id='submit-btn']")

def verify_missing_field_num(driver, num):
    utils.verify_text(driver, "Missing Field Number", "//span[@class='label label-error']", num)

def verify_ref_id_contains_value(driver):
    try:
        utils.wait_until_xpath(driver, "//td[text()='Ref ID:']/following-sibling::*[1]", 10)
        el = driver.find_element_by_xpath("//td[text()='Ref ID:']/following-sibling::*[1]")
        ref = datetime.today().strftime('%y%m')
        if ref in el.text:
            return el.text
            print("Reference ID contains number")
        else:
            pytest.fail("Reference ID does not contains anything")
    except Exception:
        pytest.fail("Failed to verify Ref ID")
    
def verify_agency_details(driver, agency):
    utils.verify_text(driver, "Agency Details", "//td[text()='Agency Details:']/following-sibling::*[1]/span[1]", agency)

def get_status(driver):
    try:
        el = driver.find_element_by_xpath("//td[text()='Status:']/following-sibling::*[1]")
        status = el.text
        print("Get Grant Status Successful")
        return status
    except Exception:
        pytest.fail("Failed to get Grant Status")

def get_submit_date(driver):
    try:
        el = driver.find_element_by_xpath("//td[text()='Submitted on:']/following-sibling::*[1]")
        date = el.text
        print("Get Submitted Date Successful")
        return date
    except Exception:
        pytest.fail("Failed to get submitted date")