#!/usr/bin/env python3

# Read from RTC, write to RTC


from datetime import datetime, timezone
import pyRPiRTC


def format_dt(dt):
    return dt.strftime('%Y.%m.%d %H:%M:%S')


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


rtc = pyRPiRTC.DS1302()
# rtc = pyRPiRTC.DS1302(ce_pin=11, data_pin=12, clk_pin=13)  # setup custom GPIO ports

# dt_now = datetime.now()  # datetime WITH timezone info
dt_now = datetime.utcnow()  # datetime without timezone info
print('Now is (UTC)', format_dt(dt_now))
# Now is (UTC) 2018.06.09 13:29:03

rtc.write_datetime(dt_now)

dt_rtc = rtc.read_datetime()
print('RTC time is:', format_dt(dt_rtc))
# RTC time is: 2018.06.09 13:29:03
print('With applied timezone info current time is:', format_dt(utc_to_local(dt_rtc)))
# With applied timezone info now is: 2018.06.09 16:29:03
