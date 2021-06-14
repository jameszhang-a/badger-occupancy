import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date, datetime
from os import path


#Finds and starts webdriver
URL = 'https://services.recwell.wisc.edu/FacilityOccupancy'
PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=PATH)
driver.get(URL)


#gets the date and time
today = date.today()
now = datetime.now()

d = today.strftime('%m/%d/%y')
t = now.strftime('%H:%M:%S')

print('Date and time: ', d, ' ' , t )

#parses content
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

#find data
name = soup.findAll(attrs='occupancy-count')[0].find('strong')

#add to pandas, then export to csv
df = pd.DataFrame({'Date': d, 'Time': t, 'Occupency': [name.text]})
if not path.exists('data.csv'):
    df.to_csv('data.csv', index=False, encoding='Utf-8')
else:
    df.to_csv('data.csv', mode='a', header=False, index=False, encoding='Utf-8')

        

    
