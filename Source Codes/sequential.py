from twitter_scraper import get_tweets
import pandas
#sh_username is  csv file having limited no of users (8) [By Muhammad Ghous 59455]
df = pandas.read_csv('sh_username.csv')

import sss
import time
start_time = time.time()#sequential start time [By Muhammad Ghous 59455]

list=[]
for i in range(8):
  usr= df["username"][i]

  
  print("Processing Tweets of : @",usr)
  j=1
  try:
    for tweet in get_tweets(usr, pages=1):
      print(j,end=" ")
      csvstring=usr+','
      post = tweet['text']
      
      csvstring +="\""+post+"\""+','
      #print(post)
      pn = sss.analysis(post)
      csvstring +=str(pn)+'\n'
      #print(pn)
      j=j+1
      list.append(csvstring)
    print("")
  except:
    j=1
# printing total time consumed  [By Muhammad Ghous 59455]
print("---Total Time in %s seconds ---" % (time.time() - start_time))

#here we are creating accuracy.csv file so that we can check our accuracy score [By Muhammad Ghous 59455]
#with open('accuracy.csv', 'a') as fd:
  #fd.writelines(list)
