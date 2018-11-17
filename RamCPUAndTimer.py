import psutil
import time

start_time = time.time()
process = psutil.Process()

print(psutil.cpu_percent(interval=0.0, percpu=True)

print(process.virtual_memory())

statsIO = process.io_counters()
print(
"""
Number of Threads: %d
Memory Utilisation: %d
CPU percentage: %d

IO: 
Read Count: %d     Read Bytes: %d
Write Count: %d     Write Bytes: %d
""" % (process.num_threads(), process.memory_info().rss, process.cpu_percent(interval=None), statsIO.read_count, statsIO.read_bytes, statsIO.write_count, statsIO.write_bytes)

)
