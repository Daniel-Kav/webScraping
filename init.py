import requests
from bs4 import BeautifulSoup

url = 'https://www.flashscore.co.ke/'

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML 
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract information about matches with a 65% chance of winning
    matches = []
    for match in soup.find_all('div', class_='coupon'):
        # Extract match details
        home_team = match.find('div', class_='teams-home').text.strip()
        away_team = match.find('div', class_='teams-away').text.strip()
        chance_of_winning = match.find('div', class_='prob1').text.strip()

        # Check if chance of winning is 65%
        if chance_of_winning == '65':
            matches.append({'Home Team': home_team, 'Away Team': away_team, 'Chance of Winning': chance_of_winning})

    # Print or use the extracted matches as needed
    for match in matches:
        print(match)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
