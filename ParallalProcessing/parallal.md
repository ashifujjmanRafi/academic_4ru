# Installation and run a code

use sudo apt-get update to update the system
use sudo apt install openmpi-bin libopenmpi-dev to install mpi
use echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope to resolve some problem (may be only for wsl)
go to your projects folder
mpicc name.c -o mpi.o (compile c file)
mpiCC name.cpp -o mpi.o (compile cpp file)
mpirun -np 4 ./mpi.o (run mpi)