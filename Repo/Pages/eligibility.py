import time
import pytest

from Pages import utils

def verify_total_qns(driver):
    try:
        el = driver.find_elements_by_xpath("//label[@class='control-label bgp-label']")
        if len(el) == 4:
            print("Total of 4 Questions verified")
        else:
            pytest.fail("Total question does not matched. Actual: "+str(len(el))+" Expected: 4")
    except Exception:
        pytest.fail("Failed to verify total number of questions")

def verify_qn1_text(driver):
    try:
        el = driver.find_elements_by_xpath("//label[@class='control-label bgp-label']")
        utils.scroll_to_element(driver, el[0])
        text = "Is the applicant registered in Singapore? *"
        if el[0].text == text:
            print("Question 1 Text verified successfully")
        else:
            pytest.fail("Question 1 text displayed incorrectly. Actual: "+el[0].text+" Expected: "+text)
    except Exception:
        pytest.fail("Failed to verify question 1 text")
    
def verify_qn2_text(driver):
    try:
        el = driver.find_elements_by_xpath("//label[@class='control-label bgp-label']")
        utils.scroll_to_element(driver, el[1])
        text = "Is the applicant's group sales turnover less than or equal to S$100m or is the applicant's group employment size less than or equal to 200? *"
        if el[1].text == text:
            print("Question 2 Text verified successfully")
        else:
            pytest.fail("Question 2 text displayed incorrectly. Actual: "+el[1].text+" Expected: "+text)
    except Exception:
        pytest.fail("Failed to verify question 1 text")

def verify_qn3_text(driver):
    try:
        el = driver.find_elements_by_xpath("//label[@class='control-label bgp-label']")
        utils.scroll_to_element(driver, el[2])
        text = "Does the applicant have at least 30% local equity? *"
        if el[2].text == text:
            print("Question 3 Text verified successfully")
        else:
            pytest.fail("Question 3 text displayed incorrectly. Actual: "+el[2].text+" Expected: "+text)
    except Exception:
        pytest.fail("Failed to verify question 1 text")

def verify_qn5_text(driver):
    try:
        el = driver.find_elements_by_xpath("//label[@class='control-label bgp-label']")
        utils.scroll_to_element(driver, el[4])
        text = "Are all the following statements true for this project? *"
        text1 = "The applicant has not started work on this project"
        text2 = "The applicant has not made any payment to any supplier, vendor, or third party prior to applying for this grant"
        text3 = "The applicant has not signed any contractual agreement with any supplier, vendor, or third party prior to applying for this grant"
        if text in el[4].text:
            print("Question 5 Question Text verified successfully")
            if text1 in el[4].text:
                print("Question 5 Point 1 Text verified successfully")
                if text2 in el[4].text:
                    print("Question 5 Point 2 Text verified successfully")
                    if text3 in el[4].text:
                        print("Question 5 Point 3 Text verified successfully")
                    else:
                        pytest.fail("Question 5 point 3 text displayed incorrectly. Actual: "+el[4].text+" Expected: "+text3)
                else:
                    pytest.fail("Question 5 point 2 text displayed incorrectly. Actual: "+el[4].text+" Expected: "+text2)
            else:
                pytest.fail("Question 5 point 1 text displayed incorrectly. Actual: "+el[4].text+" Expected: "+text1)
        else:
            pytest.fail("Question 5 question text displayed incorrectly. Actual: "+el[4].text+" Expected: "+text)
    except Exception:
        pytest.fail("Failed to verify question 1 text")

def verify_qn1_type(driver):
    utils.verify_input_type(driver, "SG Register Check Yes Radio Button", "//input[@id='react-eligibility-sg_registered_check-true']", "radio")
    utils.verify_text(driver, "SG Register Check Yes Radio Button Text", "//input[@id='react-eligibility-sg_registered_check-true']/..", "Yes")
    utils.verify_input_type(driver, "SG Register Check No Radio Button", "//input[@id='react-eligibility-sg_registered_check-false']", "radio")
    utils.verify_text(driver, "SG Register Check No Radio Button Text", "//input[@id='react-eligibility-sg_registered_check-false']/..", "No")

def verify_qn2_type(driver):
    utils.verify_input_type(driver, "Turn Over Check Yes Radio Button", "//input[@id='react-eligibility-turnover_check-true']", "radio")
    utils.verify_text(driver, "Turn Over Check Yes Radio Button Text", "//input[@id='react-eligibility-turnover_check-true']/..", "Yes")
    utils.verify_input_type(driver, "Turn Over Check No Radio Button", "//input[@id='react-eligibility-turnover_check-false']", "radio")
    utils.verify_text(driver, "Turn Over Check No Radio Button Text", "//input[@id='react-eligibility-turnover_check-false']/..", "No")

def verify_qn3_type(driver):
    utils.verify_input_type(driver, "Global HQ Check Yes Radio Button", "//input[@id='react-eligibility-global_hq_check-true']", "radio")
    utils.verify_text(driver, "Global HQ Check Yes Radio Button Text", "//input[@id='react-eligibility-global_hq_check-true']/..", "Yes")
    utils.verify_input_type(driver, "Global HQ Check No Radio Button", "//input[@id='react-eligibility-global_hq_check-false']", "radio")
    utils.verify_text(driver, "Global HQ Check No Radio Button Text", "//input[@id='react-eligibility-global_hq_check-false']/..", "No")

def verify_qn4_type(driver):
    utils.verify_input_type(driver, "New Target Market Check Yes Radio Button", "//input[@id='react-eligibility-new_target_market_check-true']", "radio")
    utils.verify_text(driver, "New Target Market Check Yes Radio Button Text", "//input[@id='react-eligibility-new_target_market_check-true']/..", "Yes")
    utils.verify_input_type(driver, "New Target Market Check No Radio Button", "//input[@id='react-eligibility-new_target_market_check-false']", "radio")
    utils.verify_text(driver, "New Target Market Check No Radio Button Text", "//input[@id='react-eligibility-new_target_market_check-false']/..", "No")

def verify_qn5_type(driver):
    utils.verify_input_type(driver, "Started Project Check Yes Radio Button", "//input[@id='react-eligibility-started_project_check-true']", "radio")
    utils.verify_text(driver, "Started Project Check Yes Radio Button Text", "//input[@id='react-eligibility-started_project_check-true']/..", "Yes")
    utils.verify_input_type(driver, "Started Project Check No Radio Button", "//input[@id='react-eligibility-started_project_check-false']", "radio")
    utils.verify_text(driver, "Started Project Check No Radio Button Text", "//input[@id='react-eligibility-started_project_check-false']/..", "No")

def answer_qn1_no(driver):
    utils.click_btn(driver, "Question1 No Radio", "//input[@id='react-eligibility-sg_registered_check-false']/..")

def verify_warning_msg(driver):
    utils.verify_text(driver, "Answer No Warning Msg", "//div[@class='eligibility-advice']", "Visit Smart Advisor on the SME Portal for more information on other government assistance.")

def verify_warning_url(driver):
    try:
        el = driver.find_element_by_xpath("//div[@class='eligibility-advice']/span/a")
        utils.scroll_to_element(driver, el)
        el_url = el.get_attribute("href")
        url = "https://www.smeportal.sg/content/smeportal/en/moneymatters.html#saText"
        if el_url == url:
            print("Verify warning url Successful")
        else:
            pytest.fail("Url mismatched. Actual: "+el_url+" Expected: "+url)
    except Exception:
        pytest.fail("Failed to verify warning url")

def select_all_qns_yes(driver):
    utils.click_btn(driver, "Question1 Yes Radio", "//input[@id='react-eligibility-sg_registered_check-true']/..")
    utils.click_btn(driver, "Question2 Yes Radio", "//input[@id='react-eligibility-turnover_check-true']/..")
    utils.click_btn(driver, "Question3 Yes Radio", "//input[@id='react-eligibility-global_hq_check-true']/..")
    utils.click_btn(driver, "Question4 Yes Radio", "//input[@id='react-eligibility-new_target_market_check-true']/..")
    utils.click_btn(driver, "Question5 Yes Radio", "//input[@id='react-eligibility-started_project_check-true']/..")

def click_save_btn(driver):
    utils.click_btn(driver, "Save Btn", "//button[@id='save-btn']")

def verify_selection_saved(driver):
    utils.verify_is_selected(driver, "Question1 Yes Radio", "//input[@id='react-eligibility-sg_registered_check-true']")
    utils.verify_is_selected(driver, "Question2 Yes Radio", "//input[@id='react-eligibility-turnover_check-true']")
    utils.verify_is_selected(driver, "Question3 Yes Radio", "//input[@id='react-eligibility-global_hq_check-true']")
    utils.verify_is_selected(driver, "Question4 Yes Radio", "//input[@id='react-eligibility-new_target_market_check-true']")
    utils.verify_is_selected(driver, "Question5 Yes Radio", "//input[@id='react-eligibility-started_project_check-true']")

def click_next_btn(driver):
    utils.click_btn(driver, "Next Btn", "//button[@id='next-btn']")