import requests
import pandas as pd

# Base API URL
url = "https://data.usaid.gov/resource/a3rc-nmf6.json"

# Set the limit to a number larger than the dataset size (10,324 rows)
limit = 10000  

# Fetch the data from the API
response = requests.get(f"{url}?$limit={limit}")

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Convert the data into a Pandas DataFrame
    df = pd.DataFrame(data)

    # Display the first few rows
    print(df.head())

    # Optionally, export the data to a CSV file
    df.to_csv('all_health_commodity_data.csv', index=False)

    print("Data fetch complete. Total records fetched:", len(df))

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
