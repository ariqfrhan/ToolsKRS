from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#=================LOGIN======================
driver = webdriver.Chrome(executable_path=r'C:\Windows\chromedriver.exe')
driver.get('https://siam.ub.ac.id/')
driver.find_element(By.XPATH, "//input[@name=\'username\']").click()
# 4 | type | xpath=//input[@name='username'] | 215150400111009
driver.find_element(By.XPATH, "//input[@name=\'username\']").send_keys("215080607111050")
# 5 | type | xpath=//input[@name='password'] | ariqfarhan11112002
driver.find_element(By.XPATH, "//input[@name=\'password\']").send_keys("140503nhk")
    # 6 | sendKeys | name=password | ${KEY_ENTER}
driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

#=========================MATKUL 1==========================================
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://siam.ub.ac.id/addcourse.php")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text").click()
    # 4 | select | css=tr:nth-child(2) > td > .text | label=Seluruh hari
dropdown = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text")
dropdown.find_element(By.XPATH, "//option[. = 'Seluruh hari']").click()
    # 5 | type | css=tr:nth-child(3) > td > .text | 123456
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys("PPP60005")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys(Keys.ENTER)

#=========================MATKUL 2==========================================
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("https://siam.ub.ac.id/addcourse.php")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text").click()
    # 4 | select | css=tr:nth-child(2) > td > .text | label=Seluruh hari
dropdown = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text")
dropdown.find_element(By.XPATH, "//option[. = 'Seluruh hari']").click()
    # 5 | type | css=tr:nth-child(3) > td > .text | 123456
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys("PPP60005")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys(Keys.ENTER)

#=========================MATKUL 2==========================================
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])
driver.get("https://siam.ub.ac.id/addcourse.php")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text").click()
    # 4 | select | css=tr:nth-child(2) > td > .text | label=Seluruh hari
dropdown = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text")
dropdown.find_element(By.XPATH, "//option[. = 'Seluruh hari']").click()
    # 5 | type | css=tr:nth-child(3) > td > .text | 123456
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys("PPP60005")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys(Keys.ENTER)

#=========================MATKUL 4==========================================
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[4])
driver.get("https://siam.ub.ac.id/addcourse.php")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text").click()
    # 4 | select | css=tr:nth-child(2) > td > .text | label=Seluruh hari
dropdown = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text")
dropdown.find_element(By.XPATH, "//option[. = 'Seluruh hari']").click()
    # 5 | type | css=tr:nth-child(3) > td > .text | 123456
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys("PPP60005")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys(Keys.ENTER)

#=========================MATKUL 5==========================================
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[5])
driver.get("https://siam.ub.ac.id/addcourse.php")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text").click()
    # 4 | select | css=tr:nth-child(2) > td > .text | label=Seluruh hari
dropdown = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text")
dropdown.find_element(By.XPATH, "//option[. = 'Seluruh hari']").click()
    # 5 | type | css=tr:nth-child(3) > td > .text | 123456
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys("PPP60005")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys(Keys.ENTER)

#=========================MATKUL 6==========================================
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[6])
driver.get("https://siam.ub.ac.id/addcourse.php")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text").click()
    # 4 | select | css=tr:nth-child(2) > td > .text | label=Seluruh hari
dropdown = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text")
dropdown.find_element(By.XPATH, "//option[. = 'Seluruh hari']").click()
    # 5 | type | css=tr:nth-child(3) > td > .text | 123456
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys("PPP60005")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys(Keys.ENTER)

#=========================MATKUL 7==========================================
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[7])
driver.get("https://siam.ub.ac.id/addcourse.php")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text").click()
    # 4 | select | css=tr:nth-child(2) > td > .text | label=Seluruh hari
dropdown = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text")
dropdown.find_element(By.XPATH, "//option[. = 'Seluruh hari']").click()
    # 5 | type | css=tr:nth-child(3) > td > .text | 123456
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys("PPP60005")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys(Keys.ENTER)

#=========================MATKUL 8==========================================
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[8])
driver.get("https://siam.ub.ac.id/addcourse.php")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text").click()
    # 4 | select | css=tr:nth-child(2) > td > .text | label=Seluruh hari
dropdown = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td > .text")
dropdown.find_element(By.XPATH, "//option[. = 'Seluruh hari']").click()
    # 5 | type | css=tr:nth-child(3) > td > .text | 123456
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys("PPP60005")
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td > .text").send_keys(Keys.ENTER)





