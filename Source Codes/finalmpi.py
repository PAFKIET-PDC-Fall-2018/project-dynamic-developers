#!/usr/bin/env python
#importing libraries [By S M Fasih Ali 60838] 
import pandas
import senti # importing senti.py [By S M Fasih Ali 60838] 
import numpy as np
from mpi4py import MPI
import sss # importing sss.py[sentiwordnet] [By S M Fasih Ali 60838] 
import time
start_time = time.time()
# ============ initilization of mpi [By S M Fasih Ali 60838] ======
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank
users = [] 

tweetdata = []

df = pandas.read_csv('sh_username.csv')
for m in range(len(df)):
    users.append(df["username"][m]) # reading from csv file and saving in users list [By S M Fasih Ali 60838] 



N = len(users)  # no of users [By S M Fasih Ali 60838] 
my_N = int(N/size) # no of users for each process/machine [By S M Fasih Ali 60838] 
N= N- N%my_N # for dividing equally [By S M Fasih Ali 60838] 
if rank == 0: # if base process or server initialize list 
    A = np.arange(N, dtype=np.int)
else:
    A = np.empty(N, dtype=np.int)

my_A = np.empty(my_N, dtype=np.int)

# Scatter data into my_A arrays


if comm.rank == 0: 
    print('scattering data at rank %d' % comm.rank)
comm.Scatter( [A, MPI.INT], [my_A, MPI.INT],root=0 ) #scattering A list [By S M Fasih Ali 60838]  
print('scraping data at rank %d' % comm.rank)
start = my_A[0] #starting index [By S M Fasih Ali 60838] 
end = my_A[len(my_A)-1] #ending index [By S M Fasih Ali 60838] 
uname = users[start:end+1] # users from starting index to ending index for eg. if rank = 4 and user = 8 then each uname contains 2 users [By S M Fasih Ali 60838] 



data = [] # list for scrape tweets [By S M Fasih Ali 60838] 
for name in uname: #for scraping tweets [By S M Fasih Ali 60838] 
  try:
    temp = senti.scrape(name,1) 
    data.append(temp)
  except:
    print("")

i = 0 # as a counter [By S M Fasih Ali 60838] 
print('showing tweets at rank %d' %comm.rank)
for tweets in data: 
    for tweet in tweets[0]: # tweets[0] = scraped tweet and tweet[1] is username [By S M Fasih Ali 60838] 

        user = ("tweet by: @ %s \n" % (tweets[1])) 
        #print(user)
        rank= ("Post#: %d and rank#: %d \n" % (i, comm.rank))
        post = tweet['text'] # fetching text from tweet [By S M Fasih Ali 60838] 
        #print(post)
        analysis = sss.analysis(post) # sentimental analysis by sentiword.net [By S M Fasih Ali 60838] 
        tweetdata.append("%s %s %s \n sentiment ::::::::::::::::  %s \n \n\n\n" %(user,rank,post,analysis)) #saving data in list [By S M Fasih Ali 60838] 
        i= i+1


print('lenght of %d data at rank %d' % (len(tweetdata),comm.rank))
comm.barrier()
if comm.rank == 0:
    print("---Total Time in %s seconds ---" % (time.time() - start_time))
    
    comm.Allgather( [my_A, MPI.int], [A, MPI.int] )
for _tweet in tweetdata: # saving analysis in text file by [rank].txt [By S M Fasih Ali 60838] 
    f = open(str(comm.rank)+".txt", "a")
    f.write(_tweet + '\n')
    # print(_tweet)




