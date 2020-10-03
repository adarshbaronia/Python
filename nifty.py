from urllib import request, error
from bs4 import BeautifulSoup as bs
import csv 

companyNameList = []
companyLinkList = []
stockNameList = []
sectorNameList = []

url = 'https://en.wikipedia.org/wiki/NIFTY_50'

nifty50_html_doc = 'nifty50_stocks.html'

htmldoc = request.urlopen(url)

if htmldoc.getcode() == 200:
    soupObject = bs(htmldoc, 'html.parser')
    soupObject.prettify()
    with open(nifty50_html_doc, 'w+', encoding='utf8') as HtmlSource:
        HtmlSource.write(soupObject.prettify())
    tabledata =soupObject.find('table', {'class': 'wikitable sortable'})
    for row in tabledata.findAll('tr')[2:]:
        companyNameList.append(row.findAll('td')[0].text)
        companyLink = row.findAll('td')[0].find('a')
        if companyLink is None:
            companyLinkList.append("Link not Available")
        else:
            companyLinkList.append(companyLink['href'])
        stockNameList.append(row.findAll('td')[1].text)
        sectorNameList.append((row.findAll('td')[2].text).strip())        
else:
    print('Given URL is Incorrect')

print(companyNameList, companyLinkList, stockNameList, sectorNameList)

with open('nifty50_stocks.csv', 'w') as nifty50Stocks:
    csv_writer = csv.writer(nifty50Stocks)
    csv_writer.writerows(zip(companyNameList,companyLinkList,stockNameList, sectorNameList))
