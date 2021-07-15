# BGP Selenium UI Testing

1. Download and install python (If your laptop does not have python)
https://www.python.org/downloads/
2. Download and install pip (If your laptop does not have python pip)
3. Download and install pytest using pip (If your laptop does not have pytest)
4. Download chrome driver file corresponding to your laptop chrome version
https://chromedriver.chromium.org/downloads
5. Open the "Repo" folder from any IDE
6. Amend the directory of the Chrome Driver in the conftest.py file to point to the downloaded chrome driver directory in step 1
7. Open each of the test_xxx.py file (Example: test_contact_details.py) from an IDE
	test_eligibility.py (User Story 1)
	test_contact_details.py (User Story 2)
	test_form_submit.py (User Story 3)
8. Open a terminal from the IDE, then type: pytest test_xxxx.py::<TEST CASE NAME> -s
	which <TEST CASE NAME> is the test case name
	Example: pytest test_contact_details.py::test_contact_letter_offer_same_main -s
