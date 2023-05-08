#include <stdio.h>
#include <mpi.h>
int main(int argc,char **argv){
    MPI_Init(&argc,&argv);
    MPI_Status  status;
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    int size;
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    int sub_array[3];
    if(rank==0){
        int a[] = {10,20};
        MPI_Send(a,2,MPI_INT,1,0,MPI_COMM_WORLD);
        MPI_Send(a,2,MPI_INT,2,0,MPI_COMM_WORLD);
        MPI_Send(a,2,MPI_INT,3,0,MPI_COMM_WORLD);

        int total = 0;
        for(int i = 0;i<3;i++){
            int psum=0;
            MPI_Recv(&psum,1,MPI_INT,MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
            total += psum;
        }printf("total is %d in rank %d \n",total,rank);
    }
    else{
        int x = 0;
        if(rank==1){
            MPI_Recv(&sub_array,2,MPI_INT,MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
            x = sub_array[0]+sub_array[1];
        }
        if(rank==2){
            MPI_Recv(&sub_array,2,MPI_INT,MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
            x = sub_array[0]-sub_array[1];
        }
        if(rank==3){
            MPI_Recv(&sub_array,2,MPI_INT,MPI_ANY_SOURCE,MPI_ANY_TAG,MPI_COMM_WORLD,&status);
            x = sub_array[0]*sub_array[1];
        }
        printf("SUBARRAY RESULT %d in rank %d \n",x,rank);
        MPI_Send(&x,1,MPI_INT,0,0,MPI_COMM_WORLD);
    }

    MPI_Finalize();

}