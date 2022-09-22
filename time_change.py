from datetime import datetime
from pytz import timezone

format = "%Y-%m-%d %H:%M:%S"

# Current time in EST
now_est = datetime.now(timezone('US/Eastern'))
print(now_est.strftime(format))

# Convert to UTC
now_utc = now_est.astimezone(timezone('UTC'))
print(now_utc.strftime(format))