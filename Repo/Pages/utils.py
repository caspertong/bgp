import time
import pytest
import csv

from random import randint

def wait_until_xpath(driver, xpath, timeout):
    wait_time = 0
    while wait_time < timeout:
        try:
            driver.find_element_by_xpath(xpath)
            return
        except:
            time.sleep(1)
            wait_time += 1
            print("waiting for the %s to be ready, sleeping another 1 second: %d of %d seconds pass" % (xpath, wait_time, timeout))
            continue
    pytest.raises("TimeoutError","timeout waiting the element: %s" % str(xpath))

def scroll_to_element(driver, elem, scroll_to=0):
    if scroll_to == 0:
        driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'center',behavior:'auto'})", elem)
    elif scroll_to == 1:
        driver.execute_script("arguments[0].scrollIntoView({block:'start',inline:'center',behavior:'auto'})", elem)
    else:
        driver.execute_script("arguments[0].scrollIntoView({block:'end',inline:'center',behavior:'auto'})", elem)

def click_form_btn(driver, name, item):
    try:
        el = driver.find_element_by_xpath("//input[@id='"+item+"']//..")
        scroll_to_element(driver, el)
        el.click()
        print("Click on "+name+" Btn Successful")
    except Exception:
        pytest.fail("Failed to click on "+name+" Btn")

def click_btn(driver, name, item, wait_time=20):
    try:
        if wait_time > 0:
            wait_until_xpath(driver, item, wait_time)
        el = driver.find_element_by_xpath(item)
        scroll_to_element(driver, el)
        el.click()
        print("Click on "+name+" Btn Successful")
    except Exception:
        pytest.fail("Failed to click on "+name+" Btn")

def input_text(driver, name, item, text):
    try:
        el = driver.find_element_by_xpath(item)
        scroll_to_element(driver, el)
        el.clear()
        el.send_keys(text)
        print("Input "+name+" Successful")
    except Exception:
        pytest.fail("Failed to Input "+name)

def input_text_without_clear(driver, name, item, text):
    try:
        el = driver.find_element_by_xpath(item)
        scroll_to_element(driver, el)
        el.send_keys(text)
        print("Input "+name+" Successful")
    except Exception:
        pytest.fail("Failed to Input "+name)

def verify_input_type(driver, name, item, type):
    try:
        el = driver.find_element_by_xpath(item)
        scroll_to_element(driver, el)
        el_type = el.get_attribute("type")
        if el_type == type:
            print("Verify "+name+" Successful")
        else:
            pytest.fail(name+" Type mismatched. Actual: "+el_type+" Expected: "+type)
    except Exception:
        pytest.fail("Failed to verify input type "+name)

def verify_text(driver, name, item, text):
    try:
        el = driver.find_element_by_xpath(item)
        scroll_to_element(driver, el)
        if el.text == text:
            print("Verify "+name+" Successful")
        else:
            pytest.fail(name+" Type mismatched. Actual: "+el.text+" Expected: "+text)
    except Exception:
        pytest.fail("Failed to verify input type "+name)

def verify_value(driver, name, item, value):
    try:
        el = driver.find_element_by_xpath(item)
        scroll_to_element(driver, el)
        if el.get_attribute("value") == value:
            print("Verify "+name+" Successful")
        else:
            pytest.fail(name+" Type mismatched. Actual: "+el.get_attribute("value")+" Expected: "+value)
    except Exception:
        pytest.fail("Failed to verify input type "+name)

def verify_is_selected(driver, name, item):
    try:
        el = driver.find_element_by_xpath(item)
        scroll_to_element(driver, el)
        if el.is_selected():
            print("Verify "+name+" is selected Successful")
        else:
            pytest.fail(name+" is not selected")
    except Exception:
        pytest.fail("Failed to verify input type "+name)

def verify_element_exist(driver, name, item):
    try:
        el = driver.find_element_by_xpath(item)
        scroll_to_element(driver, el)
        if el:
            print("Verify "+name+" exist Successful")
        else:
            pytest.fail(name+" is not exist")
    except Exception:
        pytest.fail("Failed to verify item "+name)

#Randomizer
def random_mobile():
    return "658" + '{0:07d}'.format(randint(0, 9999999))

def random_name(prefix="test"):
    return prefix + '{0:09d}'.format(randint(0, 999999999))

def random_email(prefix="testemail", tld="testacc.com"):
    return prefix + '{0:09d}'.format(randint(0, 999999999)) + '@' + tld


def read_all_test_data(test_data_file_name):
    td = []
    csv.register_dialect('myDialect',
                         delimiter=',',
                         escapechar="\\",
                         skipinitialspace=True)
    with open(test_data_file_name + '.csv', 'r', encoding='utf-8') as csvFile:
        reader = csv.DictReader(csvFile)
        for lines in reader:
            td.append(lines)
    return td

def get_testcase_test_data(testcase_id, test_data_list):
    list_data = []
    for line in test_data_list:
        if (line['natid'] == testcase_id):
            list_data.append(line)
    return list_data