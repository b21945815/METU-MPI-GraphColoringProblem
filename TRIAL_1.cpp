#include <iostream>
#include <mpi.h>
#include "sequentialAlgorithm.h"  
#include "algorithm1-basic.h"  
#include "algorithm2-basic.h"
#include "algorithm3.h"  
#include "algorithm2-parallel.h"  
#include "algorithm2-halfAsynchronous.h"  
#include "algorithm2-asynchronous.h"  
#include "algorithm1-halfAsynchronous.h"  
#include "algorithm1-asynchronous.h"  

using namespace std;
using namespace Algorithm1Basic;
using namespace Algorithm2Basic;
using namespace Algorithm3;
using namespace Algorithm2Parallel;
using namespace Algorithm2HalfAsynchronous;
using namespace Algorithm2Asynchronous;
using namespace Algorithm1HalfAsynchronous;
using namespace Algorithm1Asynchronous;

//mpiexec -n 5 TRIAL_1.exe
int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (rank == 0) {
        //runSequentialAlgorithm();
    }
    MPI_Barrier(MPI_COMM_WORLD);
    Algorithm1Basic::runAlgorithm1Basic();

    MPI_Barrier(MPI_COMM_WORLD);
    Algorithm2Basic::runAlgorithm2Basic();

    MPI_Barrier(MPI_COMM_WORLD);
    Algorithm3::runAlgorithm3();

    MPI_Barrier(MPI_COMM_WORLD);
    Algorithm2Parallel::runAlgorithm2Parallel();

    MPI_Barrier(MPI_COMM_WORLD);
    Algorithm2HalfAsynchronous::runAlgorithm2HalfAsynchronous();

    MPI_Barrier(MPI_COMM_WORLD);
    Algorithm2Asynchronous::runAlgorithm2Asynchronous();

    MPI_Barrier(MPI_COMM_WORLD);
    Algorithm1HalfAsynchronous::runAlgorithm1HalfAsynchronous();

    MPI_Barrier(MPI_COMM_WORLD);
    Algorithm1Asynchronous::runAlgorithm1Asynchronous();

    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();
    return 0;
}