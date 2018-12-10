from twitter_scraper import get_tweets  #Download twitter_scrapper library [By S M Fasih Ali 60838]
def scrape(usr,pg): # method called by finalmpi.py for scraping tweets by username [By S M Fasih Ali 60838]
  try:
    arr = get_tweets(usr,pages=pg) # get_tweets takes two argument username and number of pages max 25pgs  [By S M Fasih Ali 60838]
    return [arr,usr] #returns tweets and username [By S M Fasih Ali 60838]
  except:
    print("user is blocked") #if user is unavailabe/private or blocked throw exeption [By S M Fasih Ali 60838]
