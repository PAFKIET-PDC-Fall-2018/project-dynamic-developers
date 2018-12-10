#!/usr/bin/env python
import pandas
import senti
import numpy as np
from mpi4py import MPI
import sss
import time
start_time = time.time()

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank
users = []

tweetdata = []

df = pandas.read_csv('sh_username.csv')
for m in range(len(df)):
    users.append(df["username"][m])



N = len(users)
my_N = int(N/size)
N= N- N%my_N
if rank == 0:
    A = np.arange(N, dtype=np.int)
else:
    A = np.empty(N, dtype=np.int)

my_A = np.empty(my_N, dtype=np.int)

# Scatter data into my_A arrays


if comm.rank == 0:
    print('scattering data at rank %d' % comm.rank)
comm.Scatter( [A, MPI.INT], [my_A, MPI.INT],root=0 )
print('scraping data at rank %d' % comm.rank)
start = my_A[0]
end = my_A[len(my_A)-1]
uname = users[start:end+1]



data = []
sum = 0
for name in uname:
  try:
    temp = senti.scrape(name,1)
    data.append(temp)
  except:
    print("")

i = 0
print('showing tweets at rank %d' %comm.rank)
for tweets in data:
    for tweet in tweets[0]:

        user = ("tweet by: @ %s \n" % (tweets[1]))
        #print(user)
        rank= ("Post#: %d and rank#: %d \n" % (i, comm.rank))
        post = tweet['text']
        #print(post)
        analysis = sss.analysis(post)
        tweetdata.append("%s %s %s \n sentiment ::::::::::::::::  %s \n \n\n\n" %(user,rank,post,analysis))
        i= i+1


print('lenght of %d data at rank %d' % (len(tweetdata),comm.rank))
comm.barrier()
if comm.rank == 0:
    print("---Total Time in %s seconds ---" % (time.time() - start_time))
for _tweet in tweetdata:
    f = open(str(comm.rank)+".txt", "a")
    f.write(_tweet + '\n')
    # print(_tweet)




