import requests
from bs4  import BeautifulSoup

url = 'https://understat.com/team/Arsenal/2023'
r = requests.get(url)
print(r)
#print(r.text)

soup = BeautifulSoup(r.text,"lxml")
print(soup.div)