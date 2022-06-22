from selenium import webdriver
from selenium.webdriver.common.by import By
import math

from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

btn = browser.find_element(By.ID, 'book')
WebDriverWait(browser, 12).until(text_to_be_present_in_element((By.ID, "price"), "100"))
btn.click()
num1 = browser.find_element(By.ID, "input_value").text
num = str(math.log(abs(12 * math.sin(int(num1)))))
browser.find_element(By.ID, "answer").send_keys(num)
button2 = browser.find_element(By.ID, "solve")
button2.click()

print(browser.switch_to.alert.text)

browser.quit()


