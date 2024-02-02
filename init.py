import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://understat.com/team/Arsenal/2023'

# Send a GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the data you need from the HTML
    # (This part requires inspecting the HTML structure of the website)
    # Example: Extracting all player names
    player_names = [player.text.strip() for player in soup.select('.player-name')]

    # Create a DataFrame using pandas
    df = pd.DataFrame({'Player Names': player_names})

    # Display the DataFrame
    print(df)

    # Optionally, you can save the data to a CSV file
    df.to_csv('arsenal_players.csv', index=False)

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
