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

dfs = pd.read_html('https://www.augusta.com/masters/players/bios/Justin_Rose', header=0)
print(dfs[1])

dfs = dfs[1]

dfs = dfs.drop(columns=['Round1.10'])

dfs.to_csv('modifiedGolfTracker.csv')





#This stuff down below didn't quite get me where I was going...
#But I think it's important to have for notes

# html = urll.urlopen(url).read()
# soup = BeautifulSoup(html, features="html.parser")
# #this finds the first table available to us, which on this specific page is the one we want.
# soup = soup.find_all('table')[0]
#
#
# table = soup.find_all('tr')[2]
#
# headers = [td.text for td in table.select("tr td")]
# print(headers)
# with open("out.csv", "w") as f:
#     wr = csv.writer(f)
#     wr.writerow(headers)
#     wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tr + tr")])
#
# table = soup.find_all('tr')[3]
#
# headers = [td.text for td in table.select("tr td")]
# print(headers)
# with open("out.csv", "w") as f:
#     wr = csv.writer(f)
#     wr.writerow(headers)
#     wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tr + tr")])

#table = soup.find_all('table', class_='data2_s')
#rows = table[0].find_all('tr')









