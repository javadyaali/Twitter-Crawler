import tweepy
from tweepy import OAuthHandler

api = ''
consumer_key = 'kTP7Uog4vwlOl8RS5qvCr0GeU'
consumer_secret = '5NpBZgTJex7TkdpDILoE6FC4qmO9WEvp6zE95qWovhwAplAo5x'
access_token = '994133061049581568-FOKWPLkZTk0mdryAB6NfrGRyUB0VVSo'
access_secret = 'dHEtPkQmhcMRexk50jq3UG17bGAEAuTWYzRDzYfPta62S'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search,q='benz').items(10):

    print(tweet)
# Print out usernames of the last 10 people to use #ocean
    print('Tweet by: @' + tweet.user.screen_name)