import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shutil
import time

s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s)
# driver = webdriver.Chrome()

links = []

heading_class = 'text-title-large'
body_class = 'elfjS'

Problem_data_folder = 'PROBLEM_DATA'

def add_link_to_file(text) :
    problems_file = 'problems.txt'

    with open(problems_file, 'a', encoding='utf-8') as file :
        file.write(text)

def add_heading_to_file(text) :

    head_file = 'heading.txt'

    # write in heading.txt file
    with open(head_file, 'a', encoding='utf-8') as file :
        file.write(text + '\n')

def add_body_to_file(text, index) :
    index_folder_path = os.path.join(Problem_data_folder, str(index))

    # to create one directory, mkdir and to create full path, makedirs
    if not os.path.exists(index_folder_path) :
        os.makedirs(index_folder_path)

    body_file = os.path.join(index_folder_path, 'body.txt')

    with open(body_file, 'w', encoding='utf-8') as file :
        file.write(text)

def explore_problem(url, index) :
    driver.get(url)
    
    wait = WebDriverWait(driver, 10)

    try :
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, heading_class)))

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, body_class)))

        # find the heading and body by id 
        heading = driver.find_element(By.CLASS_NAME, heading_class)
        body = driver.find_element(By.CLASS_NAME, body_class)

        #  add heading in file 
        add_heading_to_file(heading.text)

        # add body in PROBLEM_DATA/INDEX/problem.txt
        add_body_to_file(body.text, index)

        # add link in problems.txt
        add_link_to_file(url)

        return True
    
    except :
        print("heading and body can not scrapped : ", url)
        return False

def clean_data() :
    try :
        # remove heading.txt file 
        if os.path.exists('heading.txt') :
            os.remove('heading.txt')

        # remove problems.txt
        if os.path.exists('problems.txt') :
            os.remove('problems.txt')

        # remove data folder for body
        if os.path.exists(Problem_data_folder) :
            shutil.rmtree(Problem_data_folder)
    
    except :
        pass


# clean everything for fresh scrapping 
clean_data()

# iterate for each problem
index = 1
with open('leetcode.txt', 'r') as file :
    for link in file :
        index += explore_problem(link, index)