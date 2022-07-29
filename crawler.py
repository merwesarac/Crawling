# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:31:22 2022

@author: msarac
"""

from selenium.common import exceptions    
from selenium import webdriver 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


import pandas as pd
browser = webdriver.Chrome('C:/Users/msarac/Downloads/chromedriver_win32/chromedriver.exe')
browser.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
wait = WebDriverWait(browser, 10)

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[.='SKIP']"))).click()
except TimeoutException:
    pass

desc_list=[]
prop_list=[]


cars = browser.find_elements_by_css_selector('div.card.horizontal') 
for car in cars:
    
     desc = car.find_element_by_css_selector('h2.entry-title').text 
     prop = car.find_element_by_css_selector('p').text
    
   
     desc_list.append(desc)
     prop_list.append(prop)
   
   
   
     print(desc)
     print(prop)

     #div.card-content.col.s12.m7.l8
     
     
df = pd.DataFrame(list(zip(desc_list,prop_list)),  columns=['car','prop'])


print(df)

df[['Batterie','Reichweite','Verbrauch','Ladestecker','Preis','Detail']]= df.prop.str.split(",/n",expand=True,)

df=df.drop(['prop'],axis=1)


df.to_csv('Cars_Selenium.csv',index=False)
