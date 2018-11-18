#from https://stackoverflow.com/questions/52222002/what-is-the-difference-between-time-perf-counter-and-time-process-time
def pc():
    start = time.perf_counter()
    time.sleep(1)
    print(time.perf_counter()-start)
def pt()
    start = time.process_time()
    time.sleep(1)
    print(time.time.process_time()-start)
pc()
pt()