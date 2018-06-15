"""
Given a timezone and relative time into the past, calculate and return the
start time.

Use this equation to calculate the start date:
start_date = startof(relativeUnit).subtract(relativeAmount - 1, relativeUnit)
"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import pytz


def find_relative_time(tz, rel_start, rel_unit):
    tznow = datetime.now(pytz.timezone(tz))
    print tznow

    # Calculate start of time unit
    if rel_unit == "week":
        # Default is to use Sunday as the start of the week
        # Use `weekday()` if Monday is the start of the week
        startof = tznow - timedelta(days=tznow.isoweekday())
        startof = startof.replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        UNITS = ("microsecond", "second", "minute", "hour", "day", "month")
        replacements = {}

        for unit in UNITS:
            if rel_unit == unit:
                break
            else:
                if unit == "day" or unit == "month":
                    replacements[unit] = 1
                else:
                    replacements[unit] = 0

        startof = tznow.replace(**replacements)

    # Calculate amount of time to go back
    rel_start -= 1
    if rel_start == 0:
        return startof
    else:
        if rel_unit == "second":
            return startof - timedelta(seconds=rel_start)
        elif rel_unit == "minute":
            return startof - timedelta(minutes=rel_start)
        elif rel_unit == "hour":
            return startof - timedelta(hours=rel_start)
        elif rel_unit == "day":
            return startof - timedelta(days=rel_start)
        elif rel_unit == "week":
            return startof - timedelta(weeks=rel_start)
        elif rel_unit == "month":
            return startof - relativedelta(months=rel_start)
        else: #year
            return startof - relativedelta(years=rel_start)


tz = "Australia/Sydney"

print find_relative_time(tz, 1, "year")
print find_relative_time(tz, 3, "year")
