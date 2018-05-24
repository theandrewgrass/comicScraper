#!/usr/bin/env python3

#PUT ALL PYTHON SCRIPT INTO FUNCTIONS THAT CAN BE SHARED BY MULTIPLE TASKS

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
import datetime
import os
import time

def runDriver(url):
    # Locate chromedriver executable and set environment
    chromedriver = r'"[YOUR PATH TO CHROMEDRIVER]"'
    os.environ["webdriver.chrome.driver"] = chromedriver

    # Enable adblock so ads won't affect searching
    adBlockPath = r'D:\Programming\Python\ScrapingComics\1.16.4_0'
    chrome_options = Options()
    chrome_options.add_argument('load-extension=' + adBlockPath)
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--window-size=1,1')
    #chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.create_options()

    # Load the url
    driver.get(url)

    return driver

def getRequest():
    comicRequest = input("Enter the title of the content you would like to retrieve.")

    return comicRequest

def searchComics(driver, comicRequest):
    delay=10

    try:
        # Wait until the search bar is clickable
        wait = WebDriverWait(driver, delay)
        wait.until(EC.element_to_be_clickable((By.ID, "keyword")))

        #driver.implicitly_wait(delay)
        print("Page is ready...\nSearching for content...\n")

        # Select the search bar, clear it, insert user's query, and hit enter
        selectElem = driver.find_element_by_id('keyword')
        print("Let's see what we have here...")
        selectElem.clear()
        selectElem.send_keys(comicRequest)
        selectElem.send_keys(Keys.ENTER)

        # Get HTML to print to user
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        targetTitles = soup.findAll('tr')

        # Close browser
        driver.quit()

        return targetTitles
    
    finally:
        # Close the session when finished
        print("Ending session...\nNow closing page...")
        driver.quit()

def createListComics(targetTitles):
    # Create an empty list to hold titles
    titleList = []

    # Get the titles from within the html's a tags that are within the tr tags
    for title in targetTitles:
        try:
            unformatted = title.find('a').get_text()
            formatted = " ".join(unformatted.split())
            titleList.append(formatted)        
        except:
            pass #not all a tags have content to grab

    # Sort all of the titles in alphabetical order
    titleList.sort()

    maxLineLength = 30

    print("There are %d titles returned by your search, \"%s\"." % (len(titleList), comicRequest))
    print("Here are some of the results:\n")

    for i in range(len(titleList)):
        title = (titleList[i][:maxLineLength] + '..') if len(titleList[i]) > maxLineLength else titleList[i]

        if (i % 2 == 0) or (i == 0):
            print('{:4d}. {:35s}'.format((i+1), title), end='')
        elif i % 2 != 0:
            print("%d. %s" % ((i+1), title))                          

    if len(titleList) % 2 != 0:
        print("\n")

    return titleList

def createUrlFromTitle(titleList):
    titleChoice = int(input("Type the number corresponding to the title of the content that you would like to read.\n"))

    urlString = titleList[titleChoice - 1]

    unwantedChars = ' ,.?!:;)('
    for char in unwantedChars:
        urlString = urlString.replace(char, '-')

    for dashes in urlString:
        urlString = urlString.replace('--', '-')

    url = 'http://readcomiconline.to/Comic/' + urlString

    return url

def searchFromUrl(url):

    driver = runDriver(url)
    
    delay = 10

    try:
        # Wait until the search bar is clickable -- can change this to whatever works for this part of code
        wait = WebDriverWait(driver, delay)
        wait.until(EC.element_to_be_clickable((By.ID, "keyword")))

        #driver.implicitly_wait(delay)
        print("Page is ready...\n")

        empty = input("[take a look at the site]")
        
        # Close browser
        driver.quit()
        
    finally:
        # Close the session when finished
        print("Ending session...\nNow closing page...")
        driver.quit()

######################################################################

url = 'http://readcomiconline.to/'

comicRequest = getRequest()
driver = runDriver(url)
targetTitles = searchComics(driver, comicRequest)
titleList = createListComics(targetTitles)
titleUrl = createUrlFromTitle(titleList)
searchFromUrl(titleUrl)
