from datetime import date, time, datetime, timedelta

def working_with_date():
    data_now = date.today()
    print(data_now.strftime('%Y/%m/%d'))
    data_now_str = data_now.strftime('%A %B %Y')
    print(data_now_str)
    print(type(data_now_str))
    print(type(data_now))

def working_with_time():
    time_now = time(hour=15, minute=55, second=32)
    time_now_str = time_now.strftime('%Hh:%Mm:%Ss')
    return type(time_now_str)

def working_with_datetime():
    date_time = datetime.now()
    print(date_time.strftime('%Y/%m/%d %Hh:%Mm:%Ss'))
    tuplle = ('Lunedi', ' Martedì', 'Mercoledì', 'Giovedi', 'Venerdì', 'Sabato', 'Domenica')
    created_date = datetime(2018, 10, 16, 15, 30, 20)
    date_string = '2019/01/01'
    converted_date = datetime.strptime(date_string, '%Y/%m/%d')
    new_date = converted_date + timedelta(days=1511)
    # print(date_time.strftime('%c'))
    return f"{tuplle[date_time.weekday()]} || {created_date} || {created_date.strftime('%c')} || {converted_date} || {new_date}"


if __name__ == '__main__':
    # working_with_date()
    # print(working_with_time())
    print(working_with_datetime())
