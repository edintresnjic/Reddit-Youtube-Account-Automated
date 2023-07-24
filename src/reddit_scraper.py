# Scrape best posts within day from r/nosleep
import praw
import datetime
import json
import os
import shutil
from text_to_speech import Text_To_Speech

# Initialize the Reddit API client

with open("C:/Users/edint/Python Projects/Reddit Youtube Account Automated/reddit_info.json") as f:
    reddit_data = json.load(f)

reddit = praw.Reddit(
    client_id=reddit_data['client_id'],
    client_secret=reddit_data['client_secret'],
    user_agent=reddit_data['user_agent'],
)

subreddit_name = "nosleep"
subreddit = reddit.subreddit(subreddit_name)

# Top posts from today
today = datetime.datetime.now().timestamp()
top_posts_today = subreddit.top(time_filter='month', limit=100)  # You can adjust the 'limit' as needed

count = 1
for post in top_posts_today:
    print(f'At {round(count / 1000)}%')
    if post.is_self and post.selftext: # checks if its a text post
      if len(post.selftext) > 4000: continue

      folder = fr'C:\Users\edint\Python Projects\Reddit Youtube Account Automated\src\audiofiles\video_{count}'
      try:
            if os.path.exists(folder):
                shutil.rmtree(folder)
            
            os.makedirs(folder)
      except OSError as e:
          print(f'Error: {e}')

      Text_To_Speech([post.title, post.selftext], folder)

      count += 1