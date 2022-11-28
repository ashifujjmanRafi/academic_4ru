#include <stdio.h>
#include <mpi.h>

int main(int argc,char **argv){
    MPI_Init(&argc,&argv);
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    int a = 10;
    int b = 20;
    if(rank == 0)
        printf("sum is %d\n",a+b);
    else if(rank==1)
        printf("sub id %d\n",b-a);
    else if(rank == 1)
        printf("mul id %d\n",b*a);
    else if(rank == 0)
        printf("div id %d\n",b/a);
    

    MPI_Finalize();
}