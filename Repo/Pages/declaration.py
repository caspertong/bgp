import time
import pytest

from Pages import utils

def map_all_ans(driver, ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
    if ans1 == 'Yes':
        select1 = 'true'
    else:
        select1 = 'false'
    if ans2 == 'Yes':
        select2 = 'true'
    else:
        select2 = 'false'
    if ans3 == 'Yes':
        select3 = 'true'
    else:
        select3 = 'false'
    if ans4 == 'Yes':
        select4 = 'true'
    else:
        select4 = 'false'
    if ans5 == 'Yes':
        select5 = 'true'
    else:
        select5 = 'false'
    if ans6 == 'Yes':
        select6 = 'true'
    else:
        select6 = 'false'
    if ans7 == 'Yes':
        select7 = 'true'
    else:
        select7 = 'false'
    if ans8 == 'Yes':
        select8 = 'true'
    else:
        select8 = 'false'
    if ans9 == 'Yes':
        select9 = 'true'
    else:
        select9 = 'false'
    if ans10 == 'Yes':
        select10 = 'true'
    else:
        select10 = 'false'
    ans_all_qns(driver, select1, select2, select3, select4, select5, select6, select7, select8, select9, select10)

def ans_all_qns(driver, select1, select2, select3, select4, select5, select6, select7, select8, select9, select10):
    utils.click_btn(driver, "Question 1", "//input[@id='react-declaration-criminal_liability_check-"+select1+"']")
    utils.click_btn(driver, "Question 2", "//input[@id='react-declaration-civil_proceeding_check-"+select2+"']")
    utils.click_btn(driver, "Question 3", "//input[@id='react-declaration-insolvency_proceeding_check-"+select3+"']")
    utils.click_btn(driver, "Question 4", "//input[@id='react-declaration-project_incentives_check-"+select4+"']")
    utils.click_btn(driver, "Question 5", "//input[@id='react-declaration-other_incentives_check-"+select5+"']")
    utils.click_btn(driver, "Question 6", "//input[@id='react-declaration-project_commence_check-"+select6+"']")
    utils.click_btn(driver, "Question 7", "//input[@id='react-declaration-related_party_check-"+select7+"']")
    utils.click_btn(driver, "Question 8", "//input[@id='react-declaration-debarment_check-"+select8+"']")
    utils.click_btn(driver, "Question 9", "//input[@id='react-declaration-covid_safe_check-"+select9+"']")
    utils.click_btn(driver, "Question 10", "//input[@id='react-declaration-covid_safe_ques_check-"+select10+"']")

def click_consent_check(driver):
    utils.click_btn(driver, "Consent Check Box", "//input[@id='react-declaration-consent_acknowledgement_check']")

def click_save_btn(driver):
    utils.click_btn(driver, "Save Btn", "//button[@id='save-btn']")

def click_review_btn(driver):
    utils.click_btn(driver, "Next Btn", "//button[@id='review-btn']")