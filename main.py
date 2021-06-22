from bs4 import BeautifulSoup
from datetime import date, datetime
import requests
import csv

# Goes to the url and makes a request object
URL = 'https://services.recwell.wisc.edu/FacilityOccupancy'
source = requests.get(URL).text

# Retrives the data from the source
soup = BeautifulSoup(source, 'html.parser')
data = soup.find(attrs='occupancy-count').strong.text

# Gets the date and time
today = date.today()
now = datetime.now()
d = today.strftime('%m/%d/%y')
t = now.strftime('%H:%M')

# Writes to csv
with open('data.csv', 'a') as file:
    csv_f = csv.writer(file)
    csv_f.writerow([d, t, data])