// #include <bits/stdc++.h>
#include <stdio.h>
#include <mpi.h>
// using namespace std;

int main(int argc, char *argv[])
{

    MPI_INIT(NULL, NULL);
    int rank, total_process;
    MPI_Comm_size(MPI_COMM_WORLD, &total_process);
    MPI_Comm_rank(MPI_COMM_WORLD.& rank);

    cout << "Total process " << total_process << " ITs is running in " << rank << endl;

    MPI_FINALIZE();
    return 0;
}