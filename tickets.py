import requests
from bs4 import BeautifulSoup
url='https://in.bookmyshow.com/buytickets/ags-cinemas-villivakkam/cinema-chen-ACVM-MT/20181103'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(str(soup).find("Tuesday, 6 Nov"))
for link in soup.find_all('a'):
    x = link.get('href')
    if(str(x).find('/201811') != -1):
        print(x)
