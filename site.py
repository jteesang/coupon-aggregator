import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.wholefoodsmarket.com/sales-flyer?store-id=10613"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
body_sec = soup.find('body')
main_sec = body_sec.find('main')

# parsing specific to titles of items
deals_sec = main_sec.find('section', attrs={'class': 'w-sales-tile-group'})

titles_text = []
for i in range(0,20):
	names = deals_sec.find_all('h4')[i].text
	titles_text.append(names)
	#print(titles_text[i])



# print to csv file
csv.register_dialect('myDialect', delimiter='*', quoting=csv.QUOTE_NONE, skipinitialspace=True)

with open('Whole Foods.csv', 'w') as outfile:
	f = csv.writer(outfile, delimiter=' ', quoting=csv.QUOTE_NONE, escapechar=' ')
	for line in titles_text:
		line.replace(" ", "")
		f.writerow(line.encode('utf-8').split())

outfile.close()
