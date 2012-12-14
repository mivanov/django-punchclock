django-punchclock
=================

Really simple Django middleware for catching crashed and slow requests. It "clocks in" each request when it's first
received and "clocks out" every response before it's returned, using a unique ID for correlating requests with responses.

To use it, add `punchclock.middleware.LogRequestAndResponse` as the first entry in `MIDDLEWARE_CLASSES` in your project
settings. Requests and responses will be logged to the file `/var/tmp/punchclock.log` with timestamps and unique IDs.
Request entries also list the HTTP method, path, content length (if available), and remote host. Response entries list
the response status and elapsed time.

Once you have the log, use the unique IDs to correlate requests with their responses. Any requests that don't have a
matching response must have crashed or have not yet completed. The included script `find_crashed.py` will print these
out if you run it with the log file as the argument.
