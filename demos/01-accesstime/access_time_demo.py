"""
Writing data to different places and timing it

1. to a dict - in memory
2. to files - to disk
3. to stdout - other I/O (write only)
"""
import time
from random import randrange

NUM_VALUES = 10000
VAL_MAX = 6969696969
DISK_FILE = "disk_file.txt"

mem_dict = {}


def write_to_memory(addr, val):
    mem_dict[addr] = val


def write_to_disk(addr, val):
    with open(DISK_FILE, "a") as f:
        f.write(f'"{addr!s}" : {val!s}\n')


def write_to_stdout(addr, val):
    print(f'"{addr!s}" : {val!s}')


def main():
    memory_time = 0.0
    disk_time = 0.0
    stdout_time = 0.0

    # write to memory
    start_dt = time.time()
    for addr in range(NUM_VALUES):
        val = randrange(VAL_MAX)
        write_to_memory(addr, val)
    end_dt = time.time()
    memory_time = end_dt - start_dt

    # write to disk
    start_dt = time.time()
    for addr in range(NUM_VALUES):
        val = randrange(VAL_MAX)
        write_to_disk(addr, val)
    end_dt = time.time()
    disk_time = end_dt - start_dt

    # write to stdout
    start_dt = time.time()
    for addr in range(NUM_VALUES):
        val = randrange(VAL_MAX)
        write_to_stdout(addr, val)
    end_dt = time.time()
    stdout_time = end_dt - start_dt

    # display results
    print(f"memory: {memory_time!s}")
    print(f"  disk: {disk_time!s}")
    print(f"stdout: {stdout_time!s}")


if __name__ == "__main__":
    main()
