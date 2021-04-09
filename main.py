# 4/8/21
# Script that will ideally, take information from the Augusta.com, convert an html table into a csv which I can then use
# to manipulate for a personal Master's "Fantasy Golf" application

#Using urllib and Beautiful Soup


# First imports
import pandas as pd
import numpy
import csv
from bs4 import BeautifulSoup
import urllib.request as urll

#Getting the url into the program
url = 'https://www.augusta.com/masters/players/bios/Justin_Rose'
html = urll.urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
#this finds the first table available to us, which on this specific page is the one we want.
soup.find_all('table')[0]
table = soup.find_all('tr')[2]

headers = [th.text.encode("utf-8") for th in table.select("tr th")]

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])


#table = soup.find_all('table', class_='data2_s')
#rows = table[0].find_all('tr')









