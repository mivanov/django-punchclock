from django.conf import settings
from uuid import uuid4
import datetime
import logging


log_file = getattr(settings, 'PUNCHCLOCK_LOG', '/var/tmp/punchclock.log')
logger = logging.getLogger(__name__)
hdlr = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)


class RequestMeta():
    def __init__(self):
        self._id = uuid4().hex
        self._time = datetime.datetime.now()

    def get_id(self):
        return self._id
    id = property(get_id)

    def get_time(self):
        return self._time
    time = property(get_time)

    def time_to_now(self):
        return datetime.datetime.now() - self.time


class LogRequestAndResponse(object):
    def log(self, msg):
        logger.info(msg)

    def log_request(self, meta, request):
        info = [request.META.get('REQUEST_METHOD', 'None'),
                request.get_full_path(),
                request.META.get('CONTENT_LENGTH', 'None'),
                request.META.get('REMOTE_ADDR', 'None'),
               ]
        msg = "%s %s" % (meta.id, ' '.join([unicode(i).encode('utf-8') for i in info]))
        self.log(msg)

    def log_response(self, meta, response):
        info = [response.status_code,
                meta.time_to_now(),
               ]
        msg = "%s %s" % (meta.id, ' '.join([unicode(i).encode('utf-8') for i in info]))
        self.log(msg)

    def process_request(self, request):
        request._punchclock_meta = RequestMeta()
        self.log_request(request._punchclock_meta, request)
        return None

    def process_response(self, request, response):
        self.log_response(request._punchclock_meta, response)
        return response
