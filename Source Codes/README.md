Guide:

1   install dependencies

2   run sequential.py for single processing and uncomment last lines of code so that you can save your scrap tweets, you just have to provide 
    username list in df 
    
3   you can get 40k of user data from kaggle.com

4   run userfetching after modifying it according to your data file

5   Now you can run this on distributed environment, here we are ussing collective MPI fucntion 
    scatter and AllGather 
    scatter will divide your sent buffer into received buffer
    AllGather will provide every processed data to every single node or process
    you can run this by the folling commands
    mpirun -2 np python3 finalmpi.py
    ref: https://mpi4py.readthedocs.io/en/stable/intro.html


