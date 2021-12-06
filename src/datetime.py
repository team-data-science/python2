from datetime import datetime
from datetime import timedelta
import time

# Generate datetime now
datetime_now = datetime.now()
datetime_now
# > datetime.datetime(2021, 12, 6, 22, 37, 47, 48226)

# Modify datetime now minus one hour
datetime_now_minus_one_hour = datetime_now - timedelta(hours=1)
datetime_now_minus_one_hour
# > datetime.datetime(2021, 12, 6, 21, 37, 47, 48226)
datetime_now_minus_one_hour.strftime("%d/%m/%Y %H:%M:%S")
# > '06/12/2021 21:37:47'

# Donvert datetime to epoch using timestamp()
epoch = datetime_now.timestamp()
epoch
# > 1638826667.048226
# read epoch into custom datetime and format
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
# > '2021-12-06 22:37:47'
