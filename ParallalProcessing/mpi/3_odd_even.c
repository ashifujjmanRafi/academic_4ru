#include <stdio.h>
#include <mpi.h>

int main(int argc,char **argv){
    MPI_Init(&argc,&argv);

    int rank ;
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);

    if(rank%2==0){
        printf("world ");
    }
    else if(rank%2==1){
        printf("hello ");
    }

    

    MPI_Finalize();
}