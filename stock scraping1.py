import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
url ='https://uk.finance.yahoo.com/quote/ASPL.L'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup)


from bs4 import BeautifulSoup
import requests
url = 'https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

def ParsePrice():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    price = soup.find('span', class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
    return price

while True:
    print('Stock Current Price is:' + str(ParsePrice())