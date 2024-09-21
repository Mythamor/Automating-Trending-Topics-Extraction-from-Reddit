# Import pandas and python libraries
import pandas as pd
import re
from urllib.parse import urlparse

df = pd.read_csv('../data/extracted_reddit.csv')

# Convert created_utc to datetime
df['created_utc'] = pd.to_datetime(df.created_utc, unit='s')

# Function to extract domain and subcategories
def extract_info(url):
    # Extract website source (domain)
    parsed_url = urlparse(url)
    website_source = parsed_url.netloc  # Extract domain
    
    # Extract subcategories from the path
    subcategories = parsed_url.path.split('/')[1]  # Split path into parts and remove empty strings
    #subcategories = [part for part in subcategories if part]  # Filter out empty strings
    
    return website_source, subcategories

# Apply the extraction to the 'URLs' column
df[['website_source', 'sub_categories']] = df['url'].apply(lambda url: pd.Series(extract_info(url)))


# Save the transformed data into a csv file
df.to_csv('../data/transformed_reddit.csv', index=False)

print('Data transformation completed!')