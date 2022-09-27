#include <stdio.h>
#include <mpi.h>
int main(int argc ,char **argv){
    int my_id , root_process,ierr,num_processes;
    MPI_Status status;

    ierr = MPI_Init(&argc,&argv);
    ierr = MPI_Comm_rank(MPI_COMM_WORLD,&my_id);
    ierr = MPI_Comm_size(MPI_COMM_WORLD,&num_processes);

    if(my_id == 0){
        printf("Hello World from process %d of %d\n",my_id,num_processes);
        
    }
    else if(my_id==1){

        printf("Hello World from process %d of %d\n",my_id,num_processes);
    }
    else if (my_id==2){
        printf("Hello World from process %d of %d\n",my_id,num_processes);
    }
    else{
        printf("too many processes\n");
    }
    MPI_Finalize();
}
