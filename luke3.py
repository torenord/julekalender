from datetime import date, timedelta

friday = date(1, 1, 1).weekday()
print sum((date(y, 1, 1) + timedelta(256)).weekday() == friday for y in range(1, 2015+1))
