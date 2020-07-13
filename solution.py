import requests

un_data_url = 'https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv'
response = requests.get(un_data_url)
with open("data.csv", 'wb') as f:
    f.write(response.content)
