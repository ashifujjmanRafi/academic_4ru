#include <bits/stdc++.h> 
#include <mpi.h>
using namespace std;

int main(int argc,char **argv){
    MPI_Init(&argc, &argv);

    int a = stoi(argv[1]);
    int b = stoi(argv[2]);
    int rank;

    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    if(rank==0)
        cout<<a+b<<endl;
    if(rank==3)
        cout<<"rank "<<rank<< a-b << endl;
    if(rank==1)
        cout<<"rank "<<rank<< a*b << endl;
    if(rank==2)
        cout<<"rank "<<rank<<" division "<< a/b << endl;

    MPI_Finalize();
    return 0;
}
