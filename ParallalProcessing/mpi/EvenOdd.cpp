#include <bits/stdc++.h>
#include <mpi.h>
using namespace std;

int main(int argc , char **argv){
    MPI_Init(&argc,&argv);

    int total,rank;
    MPI_Comm_size(MPI_COMM_WORLD,&total);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    
    if(rank%2)
        cout<<"In rank "<<rank<<"hello"<<endl;
    else
        cout<<"IN Rank "<<rank<<" world"<<endl;


    MPI_Finalize();
    return 0;
}
