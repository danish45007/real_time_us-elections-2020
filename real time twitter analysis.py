import tweepy
from tweepy import Stream
from tweepy import StreamListener
import json
from textblob import TextBlob
import re
import csv


consumer_key = "**************************************************"
consumer_secret = "************************************************"
access_token = "**************************************************"
access_token_secret = "***********************************************"



auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

### Get my timeline!!!1

'''twittes = api.home_timeline()

for tweet in twittes:
    print(tweet.text)'''
### Get twitts steam and do sentiment analysis


trump = 0
warren = 0

header_name = ['Trump', 'Warren']
with open('sentiment.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=header_name)
    writer.writeheader()


class Listener(StreamListener):

    def on_data(self, data):
        raw_twitts = json.loads(data)
        try:
            tweets = raw_twitts['text']

            tweets = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweets).split())
            tweets = ' '.join(re.sub('RT', ' ', tweets).split())

            blob = TextBlob(tweets.strip())

            global trump
            global warren

            trump_sentiment = 0
            warren_sentiment = 0

            for sent in blob.sentences:
                if "Trump" in sent and "Warren" not in sent:
                    trump_sentiment = trump_sentiment + sent.sentiment.polarity
                else:
                    warren_sentiment = warren_sentiment + sent.sentiment.polarity

            trump = trump + trump_sentiment
            warren = warren + warren_sentiment

            with open('sentiment.csv', 'a') as file:
                writer = csv.DictWriter(file, fieldnames=header_name)
                info = {
                    'Trump': trump,
                    'Warren': warren
                }
                writer.writerow(info)

            print(tweets)
            print()
        except:
            print('Error got')

    def on_error(self, status):
        print(status)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_stream = Stream(auth, Listener())
twitter_stream.filter(track = ['Trump', 'Warren'])
