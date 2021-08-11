import datetime
today = datetime.datetime.today()
print(f'Today is {today}')

ref_date = datetime.datetime(2020,1,7)
print(f'Your reference date is {ref_date}')

delta = today - ref_date
delta_sec = delta.total_seconds()
print(delta_sec)


