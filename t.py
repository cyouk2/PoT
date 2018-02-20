import tweepy
import os
import sys
import argparse
from collections import Counter
from fake import Fake

consumer_key = "x"
consumer_secret = "x"
access_key = "x-x"
access_secret = "x"

def main():
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_key, access_secret)
		auth.get_authorization_url()
		api = tweepy.API(auth)
	except tweepy.TweepError:
		print ('Hata')

	username = sys.argv[1]
	user = api.get_user(username)

	target = Fake(user)
	target.getMentions(api)
	spoofAccount = input("Select account: ")
	url = input("Phising URL: ")

	spoofAc = Fake(api.get_user(spoofAccount))
	spoofAc.spoofProfile(api)

	tweets = spoofAc.getTweets(api)
	fakeTweetGenerator = TweetGenerator(tweets)
	fakeTweet = fakeTweetGenerator.setup(tweets)
	fakeTweet = ".@{} {} {} .".format(username,fakeTweet, url)

	print("***********************")
	print(fakeTweet)
	print("***********************")

	api.update_status(fakeTweet)


if __name__ == "__main__":
	main()
