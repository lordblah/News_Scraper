# Python 3.4
import praw         # Python Reddit API Wrapper
import requests     # ConnectionErrors, rerunning the program.
import time         # Timer for running the bot every set amount of time

r = praw.Reddit(
    user_agent='Reddit /r/news Scraper - version 0.0.1'
               'Created by the #redditbot Reddit Slack community'
               'Designed to scrape /r/news to help identify trending news.'
                )
username, password = 'News_Scraper', '#redditbot'
r.login(username, password)
subreddit = r.get_subreddit("news")
loop_count = 0

def scrape_news():
    '''
    Scrapes the title of every news article not yet stored and records
    them into news_titles.txt
    '''
    with open('news_titles.txt','r') as cache:
        existing = cache.read().splitlines()
    
    hot_titles = subreddit.get_hot(limit=50)
    with open('news_titles.txt', 'a+') as cache:
        for title in hot_titles:
            if title not in existing:
                cache.write('{0}\n'.format(str(title)))

while True:
    try:
        scrape_news()
    except requests.ConnectionError as e:
        print(e)
        time.sleep(60)
    loop_count += 1
    print("Program loop #{0} completed successfully.".format(loop_count))
    time.sleep(1200)
