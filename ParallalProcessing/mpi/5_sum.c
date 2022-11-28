#include <stdio.h>
#include <mpi.h>

int main(int argc,char **argv){
    MPI_Init(&argc,&argv);
    int np = 3;
    int items = 12;
    int section = items/3; //vales ata time
    int sub_array[section+1];
    int root = 0;
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Status status;

    if(rank == root){
        int data[] = {1,2,3,4,5,6,7,8,9,9,1,12};

        MPI_Send(data,section,MPI_INT,1,0,MPI_COMM_WORLD);
        MPI_Send(data+section,section,MPI_INT,2,0,MPI_COMM_WORLD);
        MPI_Send(data+(section*2),section,MPI_INT,3,0,MPI_COMM_WORLD);

        int total = 0;
        for(int i =0 ;i<np;i++){
            int psum = 0;
            MPI_Recv(&psum,1,MPI_INT,MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
            total += psum;
        }
        printf("total %d \n",total);
    }
    
    else{
        int psum = 0;
        MPI_Recv(&sub_array,section,MPI_INT,MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
        for(int i = 0;i<section;i++){
            psum += sub_array[i];
        }
        printf("total sub array sum %d\n",psum);
        MPI_Send(&psum,1,MPI_INT,0,0,MPI_COMM_WORLD);
    }


    MPI_Finalize();
}