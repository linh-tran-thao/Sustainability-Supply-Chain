# Check if DataFrame is not empty
if not df.empty:
    # Export the DataFrame to a CSV file
    df.to_csv('health_commodity_data.csv', index=False)

    print("Data successfully saved as 'health_commodity_data.csv'")
else:
    print("No data to export.")
