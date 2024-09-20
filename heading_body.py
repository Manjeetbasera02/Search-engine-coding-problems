import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('./chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=s)

links = []

heading_class = ''
body_class = ''

Problem_data_folder = 'PROBLEM_DATA'

def explore_problem(url) :
    driver.get(url)
    time.sleep(5)

    # find the heading and body by id 
    heading = driver.find_element(By.CLASS_NAME, heading_class)
    body = driver.find_element(By.CLASS_NAME, body_class)

    #  create folder problem data 





def get_links_from_file() :
    problem_file = open('leetcode.txt', 'r')

    for link in problem_file :
        links.append(link)



# read all links from file 

get_links_from_file()