"""
Given a timezone and relative time into the past, calculate and return the
start time.
"""
from datetime import datetime, timedelta

import pytz

ALLOWED_UNITS = {'day', 'month', 'week', 'year'}

req_tz = raw_input("Enter timezone: ").strip() or "Australia/Sydney"
req_amt = int(raw_input("Enter amount to go back: ").strip())
req_unit = raw_input("Relative unit: ").strip().lower()

if req_tz in pytz.all_timezones:
    if req_unit in ALLOWED_UNITS:
        if req_unit == "day":
            time_diff = timedelta(days=req_amt)
        elif req_unit == "week":
            time_diff = timedelta(weeks=req_amt)
        elif req_unit == "month":
            time_diff = timedelta(weeks=(4*req_amt))
        else:
            time_diff = timedelta(weeks=(52*req_amt))
        relative_now = datetime.now(pytz.timezone(req_tz))
        print relative_now
        print relative_now - time_diff
    else:
        print "Unsupported time unit"
else:
    print "Unrecognized timezone"
