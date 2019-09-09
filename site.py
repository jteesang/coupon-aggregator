import requests
import csv
import io
from bs4 import BeautifulSoup

url = "https://www.wholefoodsmarket.com/sales-flyer?store-id=10613"
#url = "https://www.wholefoodsmarket.com/stores/cityline"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

body_sec = soup.find('body')

# print(body_sec.prettify())

main_sec = body_sec.find('main');
#print (main_sec)

deals_sec = main_sec.find('section', attrs={'class': 'w-sales-tile-group'})

titles_text = []
for i in range(0,20):
	names = deals_sec.find_all('h4')[i].text
	titles_text.append(names)
	#print(titles_text[i])

csv.register_dialect('myDialect', delimiter=' ', quoting=csv.QUOTE_NONE, skipinitialspace=True)

with open('Whole Foods.csv', 'w') as outfile:
	f = csv.writer(outfile, delimiter=' ', quoting=csv.QUOTE_NONE, escapechar=' ')
	for line in titles_text:
		line.replace(" ", "")
		f.writerow(line.encode('utf-8'))

	# for i in range(0,20):
		#f.writerow(titles_text[i].encode('utf-8'))

outfile.close()

# with open('Whole Foods.csv', 'r') as infile:
# 	reader = csv.reader(infile, dialect='myDialect')
# 	for row in reader:
# 		print(row[2])

# infile.close()

# with open('Whole Foods.csv', 'r') as file:
# 	reader = csv.reader(file)
# 	for line in reader:
# 		file.write(line[1])

# file.close()





# print(titles_text)


# content_sec = body_sec.find('div', attrs={'ui-view': 'content'})

# print(content_sec)

