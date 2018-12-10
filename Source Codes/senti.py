from twitter_scraper import get_tweets
def scrape(usr,pg):
  try:
    arr = get_tweets(usr,pages=pg)
    return [arr,usr]
  except:
    print("user is blocked")
