import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


executable_path = "/home/alejandrocoronado/Dropbox/Github/Bots/Drivers/chromedriver_74"
os.environ["webdriver.chrome.driver"] = executable_path


chrome_options = Options()
chrome_options.add_extension('burner.crx')

driver  = webdriver.Chrome(executable_path=executable_path,  chrome_options=chrome_options)
time.sleep(2)
driver.get("chrome-extension://dnnmaoecogobjdiieopljefemjdkkaja/popup.html")
time.sleep(2)
driver_windows = driver.window_handles
burner_login_window = driver_windows[0]
time.sleep(2)

#----Burner 
driver.switch_to.window(burner_login_window)
driver.find_element_by_xpath(".//*[contains(text(), 'Already have an account?')]").click()

#------Burner credentiasl
burner_login = driver.find_element_by_xpath('//*[@id="signin_email"]')
burner_login.clear()
burner_login.send_keys("cosmicwild.insta@gmail.com")

burner_pass = driver.find_element_by_xpath('//*[@id="signin_password"]')
burner_pass.clear()
burner_pass.send_keys("Mythology053")


driver.find_element_by_xpath(".//*[contains(text(), 'Login')]").click()
time.sleep(10)

url = "https://www.instagram.com/accounts/emailsignup/"
driver.get(url)

#---------- Get burner id
content = driver.page_source 
html_contet = content.split(" ")
burner_id  = [x for x in html_contet if "__burner-mail-btn" in x][0]
burner_id = burner_id.replace("id=", "")
burner_id = burner_id.replace("\"", "")
burner_id = burner_id.replace("\'", "")

try:
	burner_buttom = driver.find_element_by_xpath('//*[@id="'+ burner_id+'"]')
	burner_buttom.click()
except Exception as e:
	print(e)


name = "ALEX"
burner_full_name = driver.find_element_by_xpath('//*[@aria-label="Full Name"]')
burner_full_name.clear()
burner_full_name.send_keys(name)


username = "ALEX12412312"
burner_username = driver.find_element_by_xpath('//*[@aria-label="Username"]')
burner_username.clear()
burner_username.send_keys(username)

password = "password"
burner_password = driver.find_element_by_xpath('//*[@aria-label="Password"]')
burner_password.clear()
burner_password.send_keys(username)

next_buttom  = driver.find_element_by_xpath('//button[text()="Next"]')
next_buttom.click()

buttom18 = driver.find_element_by_xpath('//*[@id="igCoreRadioButtonageRadioabove_18"]')
buttom18.click()

next_buttom  = driver.find_element_by_xpath('//button[text()="Next"]')
next_buttom.click()
