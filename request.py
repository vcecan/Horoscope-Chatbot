import requests
from bs4 import BeautifulSoup

links=[None]*12
horoscopes=[None]*12
for i in range(12):
    links[i] =f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={str(i+1)}'

#print(links)
def extract_source(link):
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    source=requests.get(link, headers=headers).text
    return source
#print(extract_source(link))
#signs=[None]*12
#sign_array=["src-hp-aries","src-hp-taur","src-hp-gem","src-hp-canc","src-hp-leo","src-hp-virgo","src-hp-virgo","src-hp-lib","src-hp-scpo","src-hp-sag","src-hp-cap","src-hp-aqua","src-hp-pisc"]
def extract_data(source):
    soup = BeautifulSoup(source, 'html.parser')
   # names = soup.findAll("div", {"class": "storyDetails"})
    names = soup.findAll('p')
    count=0
    for j in range(12):
        for i in names:
            return(i.text)

for i in range(12):
    horoscopes[i]=(extract_data(extract_source(links[i])))
    #print(horoscopes[i])
    #print(horoscopes[i])
# soup = BeautifulSoup(responce, "lxml")
# block = soup.find_all("div", class_="storyDetails")
# print(block)