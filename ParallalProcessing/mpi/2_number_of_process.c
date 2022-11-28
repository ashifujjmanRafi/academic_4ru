#include <stdio.h>
#include <mpi.h>

int main(int argc,char **argv){
    MPI_Init(&argc,&argv);

    int np ;//number of process
    int rank;


    MPI_Comm_size(MPI_COMM_WORLD,&np);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);

    printf("i am rank %d and number of process is %d \n",rank,np);

    MPI_Finalize();
}