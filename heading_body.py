import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# s = Service('./chromedriver-win64/chromedriver.exe')

# driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome()

links = []

heading_class = 'text-title-large'
body_class = 'elfjS'

Problem_data_folder = 'PROBLEM_DATA'

def add_heading_to_file(text) :
    if not os.path.exists(Problem_data_folder) :
        os.mkdir(Problem_data_folder)

    file_path = os.path.join(Problem_data_folder, 'heading.txt')

    # write in heading.txt file
    heading_file = open(file_path, 'w')

    heading_file.write(text + '\n')

def add_body_to_file(text, index) :
    index_folder_path = os.path.join(Problem_data_folder, str(index))
    if not os.path.exists(index_folder_path) :
        os.mkdir(index_folder_path)

    file_path = os.path.join(index_folder_path, 'problem.txt')

    problem_file = open(file_path, 'w')
    problem_file.write(text)
    

def explore_problem(url, index) :
    driver.get(url)
    time.sleep(5)

    # find the heading and body by id 
    heading = driver.find_element(By.CLASS_NAME, heading_class)
    body = driver.find_element(By.CLASS_NAME, body_class)

    #  add heading in file 
    add_heading_to_file(heading.text)

    # add body in PROBLEM_DATA/INDEX/problem.txt
    add_body_to_file(body.text, index)



def get_links_from_file() :
    problem_file = open('leetcode.txt', 'r')

    for link in problem_file :
        links.append(link)



# read all links from file 

get_links_from_file()

# iterate for each problem
index  = 1
for link in links :
    explore_problem(link, index)
    index += 1