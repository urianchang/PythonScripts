"""
Given a timezone and relative time into the past, calculate and return the
start time.

Use this equation to calculate the start date:
start_date = startof(relativeUnit).subtract(relativeAmount - 1, relativeUnit)
"""
import itertools
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import pytz


def timeunit_datetime_trunc(unit, dt, isoweek_start=7):
    # type: (str, datetime.datetime, int) -> datetime.datetime
    """
    Given a datetime object round down to the beginning of a period based on a unit passed.

    :param str unit: position to truncate after
      ('year', 'month', 'week', 'day', 'hour', 'minute', 'second', 'microsecond')
    :param datetime.datetime dt: datetime to truncate
    :param int isoweek_start: Day of week considered start of week.
      1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, 7 = Sunday

    :return:
    :rtype: datetime.datetime
    """
    if unit == 'week':
        # Calculate the offset of the date's week day to the start of the week.
        # i.e. modulo the date to the beginning of a week.

        # |          Last Week        |        This Week          |
        # | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
        # | M | Tu| W | Th| F | Sa| Su| M | Tu| W | Th| F | Sa| Su|
        #
        # Thus if today is Thursday and the start of the week is Sunday, today is 4 days past the start of the week
        # Thus if today is Friday and the start of the week is Monday, today is 4 days past the start of the week
        day_offset = (dt.weekday() + 8 - isoweek_start) % 7
        return timeunit_datetime_trunc('day', dt) - timedelta(days=day_offset)

    # Else
    units = (
        # Matching unit, next parameter to 0 or begninning
        ('year', ('month', 1)),
        ('month', ('day', 1)),
        ('day', ('hour', 0)),
        ('hour', ('minute', 0)),
        ('minute', ('second', 0)),
        ('second', ('microsecond', 0)),
         # Microseconds are ignored
    )

    # 0/1 all fields after the matching datetime field.
    return dt.replace(**dict(
        i[1] for i in itertools.dropwhile(lambda x: x[0] != unit, units)
    ))


def timeunit_relativedelta(units, offset):
    # type: (str, int) -> dateutil.relativedelta.relativedelta
    if units in ('year', 'month', 'week', 'day', 'hour', 'minute', 'second'):
        return relativedelta(**{'{}s'.format(units): offset})

    # Else, unsupported
    raise ValueError('Invalid unit type: {}'.format(units))


def find_relative_time(tz, rel_start, rel_unit):
    # type: (str, int, str) -> datetime
    tznow = datetime.now(pytz.timezone(tz))
    print tznow

    # Calculate start of time unit
    # if rel_unit == "week":
    #     # Default is to use Sunday as the start of the week
    #     # Use `weekday()` if Monday is the start of the week
    #     startof = tznow - timedelta(days=tznow.isoweekday())
    #     startof = startof.replace(hour=0, minute=0, second=0, microsecond=0)
    # else:
    #     UNITS = ("microsecond", "second", "minute", "hour", "day", "month")
    #     replacements = {}
    #
    #     for unit in UNITS:
    #         if rel_unit == unit:
    #             break
    #         else:
    #             if unit == "day" or unit == "month":
    #                 replacements[unit] = 1
    #             else:
    #                 replacements[unit] = 0
    #
    #     startof = tznow.replace(**replacements)

    startof = timeunit_datetime_trunc(rel_unit, tznow)

    # Calculate amount of time to go back
    rel_start -= 1
    if rel_start == 0:
        return startof
    else:
        # if rel_unit == "second":
        #     return startof - timedelta(seconds=rel_start)
        # elif rel_unit == "minute":
        #     return startof - timedelta(minutes=rel_start)
        # elif rel_unit == "hour":
        #     return startof - timedelta(hours=rel_start)
        # elif rel_unit == "day":
        #     return startof - timedelta(days=rel_start)
        # elif rel_unit == "week":
        #     return startof - timedelta(weeks=rel_start)
        # elif rel_unit == "month":
        #     return startof - relativedelta(months=rel_start)
        # else: #year
        #     return startof - relativedelta(years=rel_start)
        return startof - timeunit_relativedelta(rel_unit, rel_start)


tz = "Australia/Sydney"
print find_relative_time(tz, 1, "second")
print find_relative_time(tz, 3, "second")
