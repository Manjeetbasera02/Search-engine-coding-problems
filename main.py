from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
s = Service("chromedriver.exe")

driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome()

url = "https://leetcode.com/problemset/all/?page="

pattern = "/problems/"
solution = "/solution"
daily_question = "?envType=daily-question&envId="
weekely_question = "?envType=weekly-question&envId"

links = []

def get_links_elements(url) :
    global cnt
    driver.get(url)

    time.sleep(7)
    # instead of time.sleep, can use webdriverwait

    links_elements = driver.find_elements(By.TAG_NAME, 'a')


    for link_element in links_elements :
        link = link_element.get_attribute('href')
        try :
            if pattern in link and  solution not in link and daily_question not in link and weekely_question not in link:
                print(link)
                links.append(link)
                
        except :
            pass

def get_links_file() :
    lc_file = open('leetcode.txt', 'w')

    print("storing all links in lc_file")

    for link in links :
        lc_file.write(link + "\n")

# iteration for 50 pages 

for page_num in range(1,51) :
    get_links_elements(url + str(page_num))

# write all links in file 

get_links_file()

driver.quit()