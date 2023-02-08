from datetime import datetime
from datetime import date
import time 
inp_date='09-01-1939'
# M D Y 
inp_date = datetime.strptime(inp_date, '%m-%d-%Y').date()
today_date = date.today()
print(today_date, inp_date)
today_date_ts = (time.mktime(today_date.timetuple()))
inp_date_ts = (time.mktime(inp_date.timetuple()))
print(abs(today_date_ts - inp_date_ts) // (24*60*60))
# 24*60*60
# 1 sent 1939 
# 30475