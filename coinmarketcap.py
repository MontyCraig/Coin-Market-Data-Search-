import requests
import json

# Define the URL for the CoinMarketCap API endpoint
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Set the parameters for the API call: start, limit, and convert
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}

# Define the headers with the 'Accepts' key set to 'application/json' and the 'X-CMC_PRO_API_KEY' key set to your API key
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '66db9c36-9775-45c4-b0f6-eb57d6aeeb90',
}

# Create a new Session and update its headers with the ones defined earlier
session = requests.Session()
session.headers.update(headers)

# Open a new text file for writing the output
with open('cryptocurrency_data.txt', 'w') as f:
    # Make the GET request using the session.get() method with the URL and parameters
    try:
        response = session.get(url, params=parameters)

        # Load the JSON data from the response
        data = json.loads(response.text)

        # Iterate through the data['data'] list and write the required information for each cryptocurrency to the text file
        for crypto in data['data']:
            f.write(f"Cryptocurrency: {crypto['name']} ({crypto['symbol']})\n")
            f.write(f"Rank: {crypto['cmc_rank']}\n")
            f.write(f"Circulating Supply: {crypto['circulating_supply']}\n")
            f.write(f"Total Supply: {crypto['total_supply']}\n")
            f.write(f"Max Supply: {crypto['max_supply']}\n")
            f.write(f"Price (USD): ${crypto['quote']['USD']['price']}\n")
            f.write(f"24h Volume (USD): ${crypto['quote']['USD']['volume_24h']}\n")
            f.write(f"Market Cap (USD): ${crypto['quote']['USD']['market_cap']}\n")
            f.write(f"Market Cap Dominance: {crypto['quote']['USD']['market_cap_dominance']}\n")
            f.write(f"Percent Change (1h): {crypto['quote']['USD']['percent_change_1h']}%\n")
            f.write(f"Percent Change (24h): {crypto['quote']['USD']['percent_change_24h']}%\n")
            f.write(f"Percent Change (7d): {crypto['quote']['USD']['percent_change_7d']}%\n")
            f.write("\n")

    except requests.exceptions.RequestException as e:
        # Handle potential errors such as ConnectionError, Timeout, or TooManyRedirects
        print(e)
