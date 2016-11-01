# URL of Source: https://www.youtube.com/watch?v=o_OZdbCzHUA
import string
import random
import tweepy
from textblob import TextBlob
import sys
filename  = open('C:/Users/cmaddox1/Desktop/MIS3640/text_mining/tweets2.txt','w') #tweets2.txt is the location that we have all prints being sent. this updates everytime the code is run
sys.stdout = filename






consumer_key = "n1sWv9RBBiL4zQWsdRYVfandn"
consumer_secret = "xc8DviZvFECGJbHVTxxwGcvM76VfskZWF8HlNyh7puK4HvBjuQ"

access_token = "1053232980-n1smbhCN7H2dJDdGSXKhtpswYj3xq1gInihAHCS"
access_token_secret = "hmF1Rk2nrlfZnoOn9VBsKDfD1pnnVPsQp0OsxBNT0SB4a"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)#this information connects to the twiiter application we made
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)




def print_tweet_text():#this function pulls and analyzes the tweets for trump
    public_tweets = api.search(q='Trump',count=100)
    print('Below is analysis of tweets mentioning Donald Trump:')
    pos=[]
    neg=[]
    neu=[]
    for tweet in public_tweets:
        tweet_string = tweet.text#this only pulls the text of the tweet for analysis
        #if tweet_string.startswith('RT')==False:  #by uncommenting this line(and indenting the below), the code will remove all retweets(RT).We decided to include them because we see them as additional data points. 
       
        #print(tweet.text.encode("utf-8")) #when you uncomment this line, all of the tweets being analyzed will be displayed. 
        analysis = TextBlob(tweet.text)
        sentiment = analysis.sentiment
        #polarity source:https://realpython.com/blog/python/twitter-sentiment-python-docker-elasticsearch-kibana/
        if sentiment.polarity < 0:
            sentiment = "negative"
        elif sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"
        #print(sentiment) #when this line is uncommented all of the sentiments associated with the tweets will appear
        #the code below is our analysis of the tweets that come in and our interpretations of the data
        if sentiment=="positive":
            pos.append(sentiment)
        if sentiment=="negative":
            neg.append(sentiment)
        if sentiment=="neutral":
            neu.append(sentiment)
    if len(pos)>len(neg) and len(pos)>len(neu):
        print('People are tweeting a positively about Trump.')
    elif len(neu)>len(pos) and len(neu)>len(neg) or len(pos)==len(neg):
        print('People are not very opinionated about Trump.')
        if len(pos)>len(neg):
            print('Excluding neutral opinion, people tend to be positive about Trump.')
        else:
            print('Excluding neutral opinion, people tend to be negative about Trump.')
    else:
        print('People are reponding negatively to Trump.')
            


    
    print('There are',len(pos), 'positive tweets.')
    print('There are', len(neg), 'negative tweets.')
    print('There are',len(neu), 'neutral tweets.')

def print_tweet_hill():#this code does the same thing as the above, but for tweets with hillary
    public_tweets = api.search(q='Clinton',count=100)
    print('Below is analysis of tweets mentioning Hillary Clinton:')
    pos=[]
    neg=[]
    neu=[]
    for tweet in public_tweets:
        tweet_string = tweet.text
        #if tweet_string.startswith('RT')==False:
        
        
        #print(tweet.text.encode("utf-8"))
        analysis = TextBlob(tweet.text)
        sentiment = analysis.sentiment
        #polarity source:https://realpython.com/blog/python/twitter-sentiment-python-docker-elasticsearch-kibana/
        if sentiment.polarity < 0:
            sentiment = "negative"
        elif sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"
        #print(sentiment)
        
        if sentiment=="positive":
            pos.append(sentiment)
        if sentiment=="negative":
            neg.append(sentiment)
        if sentiment=="neutral":
            neu.append(sentiment)
    if len(pos)>len(neg) and len(pos)>len(neu):
        print('People are tweeting a positively about Clinton.')

    elif len(neu)>len(pos) and len(neu)>len(neg) or len(pos)==len(neg):
        print('People are not very opinionated about Clinton.')
        if len(pos)>len(neg):
            print('Excluding neutral opinion, people tend to be positive about Clinton.')
        else:
            print('Excluding neutral opinion, people tend to be negative about Clinton.')    
    else:
        print('People are reponding negatively to Clinton.')
            


    
    print('There are',len(pos), 'positive tweets.')
    print('There are', len(neg), 'negative tweets.')
    print('There are',len(neu), 'neutral tweets.')

print_tweet_text()
print('\n')
print_tweet_hill()