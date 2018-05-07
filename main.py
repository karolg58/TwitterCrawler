import tweepy
from tweepy import OAuthHandler
import simplejson as json
import time
import sqlite3

def store_to_database(c, key, tweet):
    c.execute("INSERT INTO res(key, text, json) VALUES (?, ?, ?)", [key, tweet._json["text"], json.dumps(tweet._json)])
    # Save (commit) the changes
    conn.commit()
 
consumer_key = 'kQoBZkfm1B7wIdD3nRdht0k2x'
consumer_secret = '0yozuFeGcU5cTkDa4nD9kO1BoBEaChU337il7qQ8NNhG5RJ4Pf'
access_token = '993375396728012800-kNcHQdhFQVjjDW25ON38emToHWdMhF1'
access_secret = '9KXgzZtzm36GTSPhXUNvZavKGijZ0djwMzrprC4jSHm07'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

conn = sqlite3.connect('results.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS res(id INTEGER PRIMARY KEY AUTOINCREMENT, key VARCHAR(255), text VARCHAR(511), json JSON)")
conn.commit()

key = "#python"

#c = tweepy.Cursor(api.home_timeline, include_entities=True).items()
c = tweepy.Cursor(api.search, q = key, lang='en', include_entities=True).items()

nr = 0

while True:
    try:
        tweet = c.next()
        print(100*"=")
        print(nr, ")")
        print(tweet._json["text"])
        print(100*"=")
        # Insert into db
        store_to_database(cur, key, tweet)
        nr += 1
    except tweepy.TweepError:
        print('sleeping...')
        time.sleep(5*60)    #should be 15min
        continue
    except StopIteration:
        break