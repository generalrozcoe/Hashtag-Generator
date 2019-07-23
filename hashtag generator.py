# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:09:50 2019

@author: Rozcoe
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get('https://displaypurposes.com')


Tags = []
totaltags = []
def tag_search(tag):
    global totaltags
    global Tags
    search_form = driver.find_element_by_xpath("//input[1]")
    search_form.send_keys(tag)
    time.sleep(3)
    testtext = driver.find_element_by_css_selector('.resultlist-component').text
    Tags.append(testtext)
    search_form.clear()
    return testtext
    driver.close()

 

    

def first_run():
    tag_search('firemen')

def loop():
     global totaltags
     i = 0
     while i < 25:
        global goodtags
        for element in Tags:
            cleantags = element.strip('\n')  
            goodtags = cleantags.split() 
        totaltags.extend(goodtags)
        totaltags = Remove(totaltags)
        tag_search(totaltags[i])
        #print(goodtags)
        print(totaltags)
        #print(i)
        i+=1
        
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 


first_run()
loop()

    
#print(tags)
#print(goodtags)
