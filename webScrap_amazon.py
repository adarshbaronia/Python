import requests
from bs4 import BeautifulSoup
import csv

page = requests.get(
    "https://www.amazon.in/s?k=samsung+phones&rh=n%3A1389401031&ref=nb_sb_noss")
# print(page)

soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find('div', class_='s-result-list')

resultlist = content.find_all('div', class_='sg-col-inner')
# print(resultlist)

with open('output.csv', mode='w', newline='') as outputFile:
    amazon_prices = csv.writer(
        outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    amazon_prices.writerow(
        ['Name', 'Price', 'Currency', 'Stars', 'Number of Ratings'])

    for result in resultlist:
        title = result.find('h2').text.strip()
        # print(title)
        stars = result.find(
            'div', class_='a-row a-size-small').find_all('span')[0].text.strip()[:3]
        numberRatings = result.find(
            'div', class_='a-row a-size-small').find_all('span')[3].text.strip()
        price = result.find(
            'span', class_='a-price').find('span', class_='a-offscreen').text
        currency = price[:1]
        prices = price[1:]
        amazon_prices.writerow([title, prices, currency, stars, numberRatings])
        #print(currency, prices) 
