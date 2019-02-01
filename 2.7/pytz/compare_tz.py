import time
from datetime import datetime

import pytz

l = ['Australia/Sydney', 'US/Pacific', 'UTC', 'Pacific/Kiritimati']

earliest_tz = None
for tzStr in l:
    if earliest_tz is not None:
        now = datetime.now()
        tz1 = pytz.timezone(earliest_tz)
        tz2 = pytz.timezone(tzStr)
        s1 = tz1.normalize(tz1.localize(now)).utcoffset().total_seconds()
        s2 = tz2.normalize(tz2.localize(now)).utcoffset().total_seconds()
        if s2 > s1:
            earliest_tz = tzStr
    else:
        earliest_tz = tzStr

print earliest_tz

# For debugging:
# now = datetime.now()
#
# print pytz.timezone('UTC').normalize(pytz.timezone('UTC').localize(now)).utcoffset().total_seconds()
# print pytz.timezone('US/Pacific').normalize(pytz.timezone('US/Pacific').localize(now)).utcoffset().total_seconds()
# print pytz.timezone('Pacific/Kiritimati').normalize(pytz.timezone('Pacific/Kiritimati').localize(now)).utcoffset().total_seconds()
#
# print datetime.now(pytz.timezone('US/Pacific')).utcoffset().total_seconds()
# time.sleep(1)
# print datetime.now(pytz.timezone('US/Pacific')).utcoffset().total_seconds()
