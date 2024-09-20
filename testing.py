from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# For Chrome
driver = webdriver.Chrome()
time.sleep(4)

# For Firefox
# driver = webdriver.Firefox()

driver.get("https://leetcode.com/problems/median-of-two-sorted-arrays/description/")
time.sleep(7)

element = driver.find_element(By.CLASS_NAME, 'text-title-large')

print(element.text)


# print(driver.title)

driver.quit()
