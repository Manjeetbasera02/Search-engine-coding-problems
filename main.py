from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service("chromedriver.exe")

driver = webdriver.Chrome(service=s)

url = "https://leetcode.com/problemset/all/?page="

pattern = "/problems/"
solution = "/solution"
daily_question = "?envType=daily-question&envId="
weekely_question = "?envType=weekly-question&envId"

cnt = 0;

links = []

def get_links_elements(url) :
    global cnt
    driver.get(url)

    time.sleep(7)

    links_elements = driver.find_elements(By.TAG_NAME, 'a')

    time.sleep(3)

    for link_element in links_elements :
        link = link_element.get_attribute('href')
        try :
            if pattern in link and  solution not in link and daily_question not in link and weekely_question not in link:
                print(link)
                links.append(link)
                cnt += 1
                
        except :
            pass

def get_links_file() :
    lc_file = open('leetcode.txt', 'w')

    print("storing all links in lc_file")

    for link in links :
        lc_file.write(link + "\n")

# iteration for 50 pages 

for page_num in range(1,3) :
    get_links_elements(url + str(page_num))

# write all links in file 

get_links_file()



print("total = ", cnt)