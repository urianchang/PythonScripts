"""
Given a timezone and relative time into the past, calculate and return the
start time. For example, if today is May 29, 1988, then 2 days ago will be
May 27, 1988.
"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import pytz

ALLOWED_UNITS = {'day', 'month', 'week', 'year'}

req_tz = raw_input("Enter timezone: ").strip() or "Australia/Sydney"
req_amt = int(raw_input("Enter amount to go back: ").strip())
req_unit = raw_input("Relative unit: ").strip().lower()

if req_tz in pytz.all_timezones:
    if req_unit in ALLOWED_UNITS:
        relative_now = datetime.now(pytz.timezone(req_tz))
        print relative_now

        if req_unit == "day":
            relative_before = relative_now - timedelta(days=req_amt)
        elif req_unit == "week":
            relative_before = relative_now - timedelta(weeks=req_amt)
        elif req_unit == "month":
            relative_before = relative_now - relativedelta(months=req_amt)
        else:
            relative_before = relative_now - relativedelta(months=(12*req_amt))

        print relative_before
    else:
        print "Unsupported time unit"
else:
    print "Unrecognized timezone"
