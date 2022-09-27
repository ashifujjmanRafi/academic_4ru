#include <bits/stdc++.h>
#include <mpi.h>
using namespace std;

int main(int argc, char **argv)
{

    MPI_Init(NULL, NULL);
    int rank, total_process;
    MPI_Comm_size(MPI_COMM_WORLD, &total_process);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);

    cout << "Total process " << total_process << " It's  running in " << rank << endl;

    MPI_Finalize();
    return 0;
}