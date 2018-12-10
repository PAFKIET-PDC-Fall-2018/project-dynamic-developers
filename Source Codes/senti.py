from twitter_scraper import get_tweets
def scrape(usr,pgs):
  try:
    arr = get_tweets(usr,pages=pgs)
    return [arr,usr]
  except:
    print("user is blocked")
