import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.wholefoodsmarket.com/sales-flyer?store-id=10613"
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
soup1 = BeautifulSoup(page.text, 'html.parser')

body_sec = soup.find('body')
main_sec = body_sec.find('main')

body_sec1 = soup1.find('body')
main_sec1 = body_sec.find('main')


# parsing titles of items
deals_sec = main_sec.find('section', attrs={'class': 'w-sales-tile-group'})

titles_text = []
for i in range(0,20):
	names = deals_sec.find_all('h4')[i].text
	titles_text.append(names)

# print to csv file
csv.register_dialect('myDialect', delimiter='*', quoting=csv.QUOTE_NONE, skipinitialspace=True)

with open('Whole Foods.csv', 'w') as outfile:
	f = csv.writer(outfile, delimiter=' ', quoting=csv.QUOTE_NONE, escapechar=' ')
	for line in titles_text:
		line.replace(" ", "")
		f.writerow(line.encode('utf-8').split())

outfile.close()

# parsing regular prices of items
# regular_sec = main_sec.find('div', attrs={'div': 'w-sales-tile__regular-price'})

regular_text = []
for i in range(0,20):
	reg = deals_sec.find_all('div', attrs={'class': 'w-sales-tile__regular-price'})[i].text
	regular_text.append(reg)
	#print(regular_text[i])




# parsing sale prices of items
prices_sec = main_sec.find('section', attrs={'class': 'w-sales-tile-group'})

prices_text = []
for i in range(0,20):
	prices = prices_sec.find_all('span', attrs={'class':'w-sales-tile__sale-price w-header3 w-bold-txt'})[i].text
	prices_text.append(prices)
	#print (prices_text[i])

# print to csv file
csv.register_dialect('myDialect', delimiter=' ', quoting=csv.QUOTE_NONE, skipinitialspace=True)

with open('Prices.csv', 'w') as ofile:
	f = csv.writer(ofile, delimiter=' ', quoting=csv.QUOTE_NONE, escapechar=' ')
	for line in prices_text:
		line.replace(" ", "")
		f.writerow(line.encode('utf-8').split())

ofile.close()

# read Items from WholeFoods.csv into list
titles_text = []
with open('Whole Foods.csv', 'r') as infile:
	f = csv.reader(infile, delimiter= '\n')
	titles_text = list(f)

	
master = zip(titles_text, regular_text, prices_text)

with open('Whole Foods.csv', 'w') as file:
	writer = csv.writer(file)
	for row in master:
		writer.writerow(row)





