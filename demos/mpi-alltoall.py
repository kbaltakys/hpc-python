from mpi4py import MPI
import numpy as np
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4

data = np.arange(8) / 10. + rank
recv_buf = np.zeros(8)

if rank == 0:
    print("Original data")
comm.Barrier()

for r in range(size):
    if rank == r:
        print("rank ", rank, data)
        sys.stdout.flush()
    comm.Barrier()

comm.Alltoall(data, recv_buf)

comm.Barrier()
if rank == 0:
    print()
    print("Final data")
    sys.stdout.flush()
comm.Barrier()

for r in range(size):
    if rank == r:
        print("rank ", rank, recv_buf)
        sys.stdout.flush()
    comm.Barrier()


