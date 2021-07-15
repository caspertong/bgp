import time
import pytest

from Pages import utils

def input_fy_end_date(driver, date):
    utils.input_text_without_clear(driver, "FY End Date", "//input[@id='react-project_impact-fy_end_date_0']", date)


def input_proposal_field(driver, sales, investment):
    utils.input_text_without_clear(driver, "Overseas Sales", "//input[@id='react-project_impact-overseas_sales_0']", sales)
    utils.input_text_without_clear(driver, "Overseas Sales", "//input[@id='react-project_impact-overseas_sales_1']", sales)
    utils.input_text_without_clear(driver, "Overseas Sales", "//input[@id='react-project_impact-overseas_sales_2']", sales)
    utils.input_text_without_clear(driver, "Overseas Sales", "//input[@id='react-project_impact-overseas_sales_3']", sales)
    utils.input_text_without_clear(driver, "Overseas Investment", "//input[@id='react-project_impact-overseas_investments_0']", investment)
    utils.input_text_without_clear(driver, "Overseas Investment", "//input[@id='react-project_impact-overseas_investments_1']", investment)
    utils.input_text_without_clear(driver, "Overseas Investment", "//input[@id='react-project_impact-overseas_investments_2']", investment)
    utils.input_text_without_clear(driver, "Overseas Investment", "//input[@id='react-project_impact-overseas_investments_3']", investment)

def input_activity(driver, rational, nontangible):
    utils.input_text_without_clear(driver, "Rational for Projections", "//textarea[@id='react-project_impact-rationale_remarks']", rational)
    utils.input_text_without_clear(driver, "Non Tangible Benefits", "//textarea[@id='react-project_impact-benefits_remarks']", nontangible)

def verify_field_alert(driver, colour):
    utils.verify_element_exist(driver, "Rationale Alert", "//p[@id='react-project_impact-rationale_remarks-alert']")
    utils.verify_element_exist(driver, "Benefit Remark Alert", "//p[@id='react-project_impact-benefits_remarks-alert']")
    try:
        el_rat = driver.find_element_by_xpath("//p[@id='react-project_impact-rationale_remarks-alert']")
        el_rat_color = el_rat.value_of_css_property("color")
        el_remark = driver.find_element_by_xpath("//p[@id='react-project_impact-benefits_remarks-alert']")
        el_remark_color = el_rat.value_of_css_property("color")
        if el_rat_color == colour and el_remark_color == colour:
            print("Color Red of the alert matched.")
        else:
            pytest.fail("Color is not matched. Expected: "+colour+" Actual: Rational is "+el_rat_color+" and Remark is "+el_remark_color)
    except Exception:
        pytest.fail("Failed to verify color alert")

def verify_section_tab_active(driver):
    try:
        el = driver.find_element_by_xpath("//span[text()='Business Impact']/../..")
        active = el.get_attribute("class")
        if active == 'active':
            print("Business Impact Section Selection")
        else:
            pytest.fail("Business Impact Section is not Selected")
    except Exception:
        pytest.fail("Failed to verify Business Impact Section Tab")

def click_save_btn(driver):
    utils.click_btn(driver, "Save Btn", "//button[@id='save-btn']")

def click_next_btn(driver):
    utils.click_btn(driver, "Next Btn", "//button[@id='next-btn']")