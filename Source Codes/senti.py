from twitter_scraper import get_tweets

import classifier

usr= 'realDonaldTrump'

for tweet in get_tweets(usr, pages=1):
    print("tweet by: @",usr)
    print("Post:")
    post = tweet['text']
    print(post)
    pn = classifier.classify(post)

    print(pn[0])
    print(pn[1])

    input()


