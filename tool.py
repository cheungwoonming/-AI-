import datetime


def date_range(begin_date, end_date, format='%Y-%m-%d'):
    dates = []
    dt = datetime.datetime.strptime(begin_date, format)
    date = begin_date[:]
    while date <= end_date:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime(format)
    return dates
