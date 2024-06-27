import requests
import pandas as pd
from io import StringIO


osf_url = "https://osf.io/download/dwztp/"
response = requests.get(osf_url)


# Check if the request was successful
if response.status_code == 200:
    # Convert the response content to a pandas DataFrame
    data = pd.read_csv(StringIO(response.text), delimiter = ';')
    
    # Display the first few rows of the DataFrame
    print(data.head())
else:
    print(f"Failed to download the dataset. Status code: {response.status_code}")

data = pd.read_csv(StringIO(response.text), delimiter=';')

data.to_csv("01_build/03_output/concho.csv")
