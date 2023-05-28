from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from twocaptcha import TwoCaptcha
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver_path = r'C:\Users\Shreyas K S\Downloads\chromedriver.exe' #path to my chromedriver

filename = "details.txt"

with open(filename, "w") as fp:
    pass

service = Service(driver_path)

driver = webdriver.Chrome(service=service)

API_KEY = ''

solver = TwoCaptcha(API_KEY)
url = 'https://ceoelection.maharashtra.gov.in/searchlist/SearchPDF.aspx'
driver.get(url)

first_dropdown = Select(driver.find_element(By.ID, 'ctl00_Content_DistrictList'))
first_dropdown.select_by_visible_text('Palghar')

second_dropdown = Select(driver.find_element(By.ID, 'ctl00_Content_AssemblyList'))
options = second_dropdown.options

for index in range(1, len(options)):
    second_dropdown = Select(driver.find_element(By.ID, 'ctl00_Content_AssemblyList'))
    option = second_dropdown.options[index]
    option_text = option.text
    print(option_text)
    second_dropdown.select_by_visible_text(option_text)

    wait = WebDriverWait(driver, 5)
    second_option_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_Content_PartList')))
    second_option_dropdown = Select(second_option_dropdown)
    final_options = second_option_dropdown.options
    with open(filename, "a") as fp:
        for final_option in final_options[1:]:
            print(final_option.text)
            fp.write(final_option.text+"\n")

# for option in options:
    # print(option.text)
# first_option_dropdown = Select(driver.find_element(By.ID, 'ctl00_Content_AssemblyList'))
# for option in options:
#     # print(option.text)
#     # second_dropdown.select_by_visible_text(option.text)
#     #
#     # second_option_dropdown = Select(driver.find_element(By.ID, 'ctl00_Content_PartList'))
#     # final_options = second_option_dropdown.options
#     # for final_option in final_options[1:]:
#     #     print(final_option.text)
#
#     print(option.text)
#     second_dropdown = Select(driver.find_element(By.ID, 'ctl00_Content_AssemblyList'))  # Re-find the second dropdown
#     second_dropdown.select_by_visible_text(option.text)
#
#     wait = WebDriverWait(driver, 5)
#     second_option_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_Content_PartList')))
#     second_option_dropdown = Select(second_option_dropdown)
#     final_options = second_option_dropdown.options
#     for final_option in final_options[1:]:
#         print(final_option.text)


# for index in range(1, options):
# for option in options:
#
#     second_dropdown = Select(driver.find_element(By.ID, 'ctl00_Content_AssemblyList'))
#     option = second_dropdown.options[index]
#     option_text = option.text
#     print(option_text)
#     # second_dropdown.select_by_visible_text(option_text)
#     # # Get the CAPTCHA image from the page
#     # # input_element = driver.find_element(By.ID, 'ctl00_Content_txtcaptcha')
#     # # parent_element = input_element.find_element(By.XPATH, '../..')
#     # # captcha_image_element = parent_element.find_element(By.TAG_NAME, 'img')
#     # captcha_image_element = driver.find_element(By.CSS_SELECTOR, ".bordered img")
#     # captcha_image_url = captcha_image_element.get_attribute('src')
#     # response = requests.get(captcha_image_url)
#     # captcha_image = response.content
#     #
#     # result = solver.solve(captcha_image)
#     #
#     # # Wait for the CAPTCHA to be solved
#     # while not result['status'] == 'ready':
#     #     time.sleep(1)
#     #     result = solver.get_result(result['task_id'])
#     #
#     # captcha_response = result['solution']['gRecaptchaResponse']
#     #
#     # # Enter the solved CAPTCHA response in the input field
#     # captcha_input = driver.find_element(By.ID, 'g-recaptcha-response')
#     # driver.execute_script("arguments[0].style.display = 'block';", captcha_input)
#     # captcha_input.send_keys(captcha_response)
#     #
#     # # Submit the CAPTCHA and wait for the form to load
#     # submit_button = driver.find_element(By.ID, 'id="ctl00_Content_OpenButton"')
#     # submit_button.click()
#     # # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_Content_SearchForm')))
#
#     wait = WebDriverWait(driver, 5)
#     second_option_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_Content_PartList')))
#     second_option_dropdown = Select(second_option_dropdown)
#     final_options = second_option_dropdown.options
#     for final_option in final_options[1:]:
#         print(final_option.text)

