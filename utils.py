import json
import datetime


class DateTimeJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        else:
            return super(DateTimeJsonEncoder, self).default(o)
