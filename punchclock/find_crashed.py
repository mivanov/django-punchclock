# This is a script for processing a "punch clock" log file that has one line
# for every request and another line for the matching response. It will output
# only those requests that don't have a response. That means they crashed or
# never completed.
import sys
if len(sys.argv) != 2:
    print "Specify the log file"
    sys.exit(1)

log_file = sys.argv[1]

requests = {}

for line in open(log_file, 'r'):
    parts = line.split(' ')
    id = parts[3]
    if id in requests:
        del requests[id]
    else:
        requests[id] = line.strip()

for r, line in requests.items():
    print line

print "%d crashed requests found." % len(requests) 