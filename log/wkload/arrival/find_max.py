import sys

fname = sys.argv[1]
max_wait = 0

with open(fname, 'r') as flog:
    lines = flog.readlines();
    for line in lines:
        items = line.split()
        wait = long(items[1]) + long(items[5])
        if wait > max_wait:
            max_wait = wait

print max_wait
