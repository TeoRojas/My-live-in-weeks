import datetime

def birth_date_to_dic(birth_date):
    birth = {
        'day' : int(birth_date.split('-')[2]),
        'month' : int(birth_date.split('-')[1]),
        'year' : int(birth_date.split('-')[0])
    }
    return birth

def days_lived(year, month, day):
    days_lived = int(str(
        datetime.datetime.now() - datetime.datetime(
            year=year, 
            month=month, 
            day=day
            )
        ).split(' ')[0]   
    )

    return days_lived

