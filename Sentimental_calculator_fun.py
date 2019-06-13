import tweepy
from textblob import TextBlob
consumer_key = 'vo2BkG5putoxUz5aQuMJ4Vkfp'
consumer_secret = 'mgUJXBrj0fWtPRGaViKCy8SSHgHdnnn1IjcHtEbzbsdpHxMojH'

access_token = '1031112367134793728-FuRYkSnb6xCwB0dC1wvyHAC8BUCSwR'
access_token_secret = '6uEQPErybgeTPaSRqB5W5mY8Sm6YKKsGKXoTWXG0jGtdm'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api =tweepy.API(auth)

print("Enter the name you want to review about")
x = input(">>")
public_tweet = api.search(x)

g=0
b=0
a=0
count = 0;
for tweet in public_tweet :

    print("Tweet no.",count,"--->")
    print(tweet.text)
    print("\n")
    result_analysis = TextBlob(tweet.text)
    k = result_analysis.sentiment.polarity
    count = count + 1
    #print(k)
    if k<0 :
        b=b+1
    elif k>0.1 :
        g = g + 1
    else :
        a = a + 1




if a>b and a>g :
    print("Average")
elif b>a and b>g :
    print("Bad Impact")
else :
    print("Good Impact")




