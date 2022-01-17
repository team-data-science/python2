from datetime import datetime
from datetime import timedelta
import time

# go through this in command line (python3)

# Generate datetime now
datetime_now = datetime.now()
print(datetime_now)
# > datetime.datetime(2021, 12, 6, 22, 37, 47, 48226)

# Modify datetime now minus one hour
datetime_now_minus_one_hour = datetime_now - timedelta(hours=1)
print(datetime_now_minus_one_hour)
# > datetime.datetime(2021, 12, 6, 21, 37, 47, 48226)

# delete the decimals from the timestamp
datetime_minus_one_reformatted = datetime_now_minus_one_hour.strftime("%d/%m/%Y %H:%M:%S")
print(datetime_minus_one_reformatted)
# > '06/12/2021 21:37:47'

# Convert datetime to epoch using timestamp()
epoch = datetime_now.timestamp()
print(epoch)
# > 1638826667.048226

# turn epoch into custom datetime and format
ts_from_epoch = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
print(ts_from_epoch)
# > '2021-12-06 22:37:47'
