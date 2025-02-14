import requests

# Base API URL
url = "https://data.usaid.gov/resource/a3rc-nmf6.json"

# Set the limit to a number larger than the dataset size (10,000 rows)
limit = 10000

# Fetch the data from the API
response = requests.get(f"{url}?$limit={limit}")

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Display the first 5 entries of the JSON data to inspect the structure
    print("First 5 entries in the dataset:")
    print(data[:5])  # Display the first 5 records

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
