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

#print('getting user')
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


