import requests
url = 'https://understat.com/team/Arsenal/2023'
r = requests.get(url)
print(r.status_code, r.headers)
#print(r.text)