import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.chrome.service as service

CHROME_DRIVER_PATH = '/Users/lz/Downloads/chromedriver'
FABRIC_URL = 'https://www.fabric.io/security2/android/apps/com.fasttrack.security/issues?status=all&event_type=crash&time=last-seven-days&subFilter=state&state=all&build%5B0%5D=1.3.4%20%2853%29'
FABRIC_ACCOUNT_NAME = 'zhe.li.1@ihandysoft.com'
FABRIC_ACCOUNT_PWD = '********'
ISSUE_KEYWORD = 'CrashGuard'

service = service.Service(CHROME_DRIVER_PATH)
service.start()
capabilities = {}
driver = webdriver.Remote(service.service_url, capabilities)

driver.get(FABRIC_URL)
time.sleep(1)
search_box = driver.find_element_by_name('email')
search_box.send_keys(FABRIC_ACCOUNT_NAME)
pwd = driver.find_element_by_name('password')
pwd.send_keys(FABRIC_ACCOUNT_PWD)

signIn = driver.find_element_by_class_name('sign-in')
print signIn.text
signIn.click()

element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'query-term')))
time.sleep(1.5)
element.send_keys(ISSUE_KEYWORD)
time.sleep(1.5)
element.send_keys(Keys.ENTER)

element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'i_issue')))
time.sleep(1.5)
issues = driver.find_elements_by_class_name('i_issue')
issues[1].click()

element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'green')))
time.sleep(1.5)
element.click()

outputFile = open('output.txt', 'w')
while 1:
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'padding-right-10px')))

    raw_text_btn = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'icon-code')))
    raw_text_btn.click()
    time.sleep(1.5)

    try:
        raw_code = driver.find_element_by_class_name('raw-code')
        print raw_code.text
        segment = driver.find_element_by_class_name('segment')
        print segment.text
        outputFile.write(raw_code.text + '\n')
        outputFile.write(segment.text + '\n\n')
    except Exception:
        continue

    element.click()
    time.sleep(1.5)


# time.sleep(15)
# driver.quit()
