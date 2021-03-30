#! venv/bin/python3
import os
import uuid
from faker import Faker
fake = Faker()
from random import randint, choice
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(f"https://dev.im-bank.bankbuddy.me/auth/rwanda/account_open.html?channel_id={str(uuid.uuid4())}")


# Helper for the dropdown menu
def select_dropdown(element, size):
    Select(element).select_by_index(randint(0, size - 1))


# page zero
driver.find_element_by_css_selector("#configure_save").click()

# First Page, Personal Details
salutation = driver.find_element_by_css_selector('#Salutation')
first_name = driver.find_element_by_css_selector('#FirstName')
middle_name = driver.find_element_by_css_selector('#MiddleName')
last_name = driver.find_element_by_css_selector('#LastName')
gender = driver.find_element_by_css_selector('#Gender')
dob = driver.find_element_by_css_selector('#DateOfBirth')
nationality = driver.find_element_by_css_selector('#Nationality')
marital_status = driver.find_element_by_css_selector('#MaritalStatus')
employment_status = driver.find_element_by_css_selector('#EmploymentStatus')
segmentation_class = driver.find_element_by_css_selector('#SegmentationClass')
occupation = driver.find_element_by_css_selector("#Occupation")
next_first_page = driver.find_element_by_css_selector('#personal_save')

select_dropdown(salutation, 3)
first_name.send_keys(fake.unique.first_name())
middle_name.send_keys(fake.unique.first_name())
last_name.send_keys(fake.unique.last_name())
select_dropdown(gender, 3)
dob.send_keys(f"{randint(1, 29)}/{randint(1, 13)}/{randint(1900, 2021)}")
select_dropdown(nationality, 4)
select_dropdown(marital_status, 4)
select_dropdown(employment_status, 3)
select_dropdown(segmentation_class, 3)
occupation.send_keys(fake.job())
next_first_page.click()

driver.implicitly_wait(5)

# Second Page, Address Page
addr_1 = driver.find_element_by_css_selector('#AddrLine1')
addr_2 = driver.find_element_by_css_selector('#AddrLine2')
province = driver.find_element_by_css_selector('#State')
district = driver.find_element_by_css_selector('#City')
sector = driver.find_element_by_css_selector('#BuildingLevel')
cell = driver.find_element_by_css_selector('#Suburb')
village = driver.find_element_by_css_selector('#StreetNum')
postal_code = driver.find_element_by_css_selector('#PostalCode')
address_category = driver.find_element_by_css_selector('#AddrCategory')
send_mail_yes = driver.find_element_by_css_selector("#send_mail_yes")
send_mail_no = driver.find_element_by_css_selector("#send_mail_no")
preferred_addr_yes = driver.find_element_by_css_selector("#preferred_yes")
preferred_addr_no = driver.find_element_by_css_selector("#preferred_no")
default_addr = driver.find_element_by_css_selector('#DefaultAddrType')
next = driver.find_element_by_css_selector('#rwandaAdd_save')

addr_1.send_keys(fake.street_name())
addr_2.send_keys(fake.street_name())
province.send_keys(fake.street_suffix())
district.send_keys(fake.city())
sector.send_keys(fake.city_suffix())
cell.send_keys(fake.building_number())
village.send_keys(fake.building_number())
postal_code.send_keys(fake.postcode())
address_category.send_keys(fake.address())
default_addr.send_keys(fake.city_suffix())
choice([send_mail_no, send_mail_yes]).click()
choice([preferred_addr_yes, preferred_addr_no]).click()
next.click()

driver.implicitly_wait(5)

'''
# Open Account, Third Page
addr_1 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[4]/div[1]/div[2]/input')
addr_2 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[4]/div[2]/div[2]/input')
addr_3 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[4]/div[3]/div[2]/input')
city = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[4]/div[4]/div[2]/input')
state = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[4]/div[5]/div[2]/input')
country = driver.find_element_by_css_selector('#Country')
postal_code = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[4]/div[7]/div[2]/input')
address_category = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[4]/div[8]/div[2]/input')
preferred_addr_yes = driver.find_element_by_css_selector("#preferred2_yes")
preferred_addr_no = driver.find_element_by_css_selector("#preferred2_no")
next = driver.find_element_by_css_selector('#countryAdd_save')

addr_1.send_keys(fake.street_name())
addr_2.send_keys(fake.street_name())
addr_3.send_keys(fake.street_name())
city.send_keys(fake.city())
state.send_keys(fake.city())
country.send_keys(fake.country())
postal_code.send_keys(fake.postcode())
address_category.send_keys(fake.address())
choice([preferred_addr_yes, preferred_addr_no]).click()
next.click()

driver.implicitly_wait(4)
'''

# Fourth Page
email = driver.find_element_by_css_selector("#Email")
mobile_number = driver.find_element_by_css_selector("#PrimaryPhone")
second_number = driver.find_element_by_css_selector("#SecondaryPhone")
second_number_yes = driver.find_element_by_css_selector("#primary_no")
second_number_no = driver.find_element_by_css_selector("#second_no")
next = driver.find_element_by_css_selector("#contact_save")

email.send_keys(fake.email())
mobile_number.send_keys(randint(50000000000, 99999999999))
choice([second_number_yes, second_number_no]).click()
second_number.send_keys(randint(50000000000, 99999999999))
next.click()

driver.implicitly_wait(5)

# Fifth Page
preferred_branch = driver.find_element_by_css_selector("#PrimarySolId")
sms_banking_yes = driver.find_element_by_css_selector("#sms_yes")
sms_banking_no = driver.find_element_by_css_selector("#sms_no")

ebanking_yes = driver.find_element_by_css_selector("#ebank_yes")
ebanking_no = driver.find_element_by_css_selector("#ebank_no")

next = driver.find_element_by_css_selector("#banking_save")

preferred_branch.send_keys(fake.city())
choice([sms_banking_yes, sms_banking_no]).click()
choice([ebanking_yes, ebanking_no]).click()
next.click()

driver.implicitly_wait(5)

# Sixth Page
national_doc_type = driver.find_element_by_css_selector("#docType")
national_id = driver.find_element_by_css_selector("#ReferenceNum")
document_image = driver.find_element_by_css_selector("#doc")
upload = driver.find_element_by_css_selector("#upload_main")

select_dropdown(national_doc_type, 1)
national_id.send_keys(randint(1235135232, 124332419432))

document_image.send_keys(os.path.abspath("a.jpeg"))
upload.click()

# Seventh Page
document_image.send_keys(os.path.abspath("b.jpg"))
upload.click()

# Eight Page
signature = driver.find_element_by_css_selector("#signature_image")
tnc = driver.find_element_by_css_selector("#TNC")
privacy_policy = driver.find_element_by_css_selector("#PrivacyPolicy")
submit = driver.find_element_by_css_selector("#undefined")

signature.send_keys(os.path.abspath("c.png"))
tnc.click()
privacy_policy.click()
submit.click()
