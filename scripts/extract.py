# Import libraries
import pandas as pd
import praw
import json
from datetime import datetime
import os
from dotenv import load_dotenv


# Load env variable
load_dotenv(override=True)


# Reddit API credentials
reddit = praw.Reddit(
                    client_id=os.getenv("REDDIT_CLIENT_ID"),
                    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Extract data from subreddit instance
# Create empty list
data = []

print('Extracting data from Reddit...')
# Loop over topics in hot category
for submission in reddit.subreddit("ai+technology+politics").hot(limit=1000):

    # Create a data dictionary
    data.append({
        
        "id":submission.id,
        "title":submission.title,
        "author": submission.author.name if submission.author else "[deleted]",
        "subreddit": submission.subreddit.display_name,
        "score":submission.score,
        "num_comments": submission.num_comments,
        "created_utc": submission.created_utc,
        "url":submission.url
    })

print('Data extraction completed!')
# Load extracted data into a pandas dataframe
df = pd.DataFrame(data)

# Save the extracted data into a csv file
df.to_csv('../data/extracted_reddit.csv', index=False)

