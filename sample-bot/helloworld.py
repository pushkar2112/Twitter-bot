#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy , time, sys

# argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'x0yYGC0LQ9FhWy5UKtjJVtXl0'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'kdjTFmDL8AbkYbGg24pt7OSlYUZfO3nHaARerCu4s0ClMjJhzw'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1460581228160045059-HebRGY4WXVqvILsMUAR5lGTzh0TuX2'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'p0t9sPA8cLRSPdoQffCuTqbGoE0Dvys5haF3X5weMWzu9'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#api.get_followers()
#auth.secure = True

#api.update_status('Hello, World!!')

# filename=open(argfile,'r')
# f=filename.readlines()
# filename.close()

# for line in f:
#     api.update_status(line)
#     time.sleep(900)#Tweet every 15 minutes

#api.create_friendship(screen_name = 'Pushkar_test',user_id = "pushkar_test", follow = False)
#api.update_status("Hello @Pushkar_test")
#api.destroy_friendship(screen_name = "Pushkar_test",user_id = "pushkar_test")
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(tweet.text, tweet.id)
#api.destroy_status(tweet.id)