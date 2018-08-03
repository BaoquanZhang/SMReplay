import sys
import random

intervals = [10, 30, 50, 100] # ms
n_zones = 1024
iosize = 1024 * 1024 / 512 # 1MB in sectors
write_size = 35 * 1024 * 1024 * 1024 /512 # 35GB in sectors
offset = 64 * 256 * 1024 * 1024 / 512 # sector
upperbound = n_zones * 256 * 1024 * 1024 / 512 # sector
i = 0;

while i < 4:
    interval = intervals[i]
    i += 1
    trace_name = '35GB_1MB_' + str(interval) + 'ms_1024_10p.trace'
    tmp_size = write_size
    with open(trace_name, 'w') as trace_f:
        time = 0;
        line_count = 0
        read_list = []
        rw = 0
        while tmp_size > 0:
            time += interval;
            if line_count % 10 == 0:
                lba = randint(0, offset) # sequential write
                rw = 1
                read_list.append(lba)
            elif line_count % 10 == 4:
                lba = randint(offset, upperbound) # non-sequential write
                rw = 1
                read_list.append(lba)
                tmp_size -= iosize
            else:
                lba = read_list[random.randint(0, len(read_list)) - 1]
                rw = 0
            line_count += 1
            line = str(time) + " " + str(lba) + " " + str(iosize) + " " + str(rw) + "\n"
            #print str(line)
            trace_f.write(line)
