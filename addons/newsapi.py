import requests
import json

# Define the API URL
url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=adbf30f0346943d2b2cd50b2928e618e"

# Make the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Define the file name for the JSON file
    filename = "news_response.json"

    # Write JSON data to a file
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"JSON response has been saved to {filename}")
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
