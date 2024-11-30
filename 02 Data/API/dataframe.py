import pandas as pd

# Check if data was fetched successfully
if response.status_code == 200:
    # Convert the JSON data into a Pandas DataFrame
    df = pd.DataFrame(data)

    # Display the first few rows of the DataFrame to verify
    print("First 5 rows of the DataFrame:")
    print(df.head())
else:
    print("No data to convert to DataFrame.")
