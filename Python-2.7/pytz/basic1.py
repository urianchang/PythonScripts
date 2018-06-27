from datetime import datetime

import pytz


pst = pytz.timezone('US/Pacific')
naive = datetime.now()
sydney = datetime.now(tz=pytz.timezone('Australia/Sydney'))

# print naive
# print pst.localize(naive)
# print pst.localize(sydney)  # ValueError: Not naive datetime
# print naive.astimezone(pytz.UTC)    # ValueError: astimezone() can't be applied to naive datetime
print pst.localize(naive).astimezone(pytz.UTC)
print pytz.UTC.localize(naive)
print pst.localize(naive).astimezone(pytz.UTC) == pytz.UTC.localize(naive)  # False
