import datetime
import os
import platform 

def birth_date_to_dic(birth_date):
    birth = {
        'day' : int(birth_date.split('-')[2]),
        'month' : int(birth_date.split('-')[1]),
        'year' : int(birth_date.split('-')[0])
    }
    return birth

def return_days_lived(year, month, day):
    days_lived = int(str(
        datetime.datetime.now() - datetime.datetime(
            year=year, 
            month=month, 
            day=day
            )
        ).split(' ')[0]   
    )

    return days_lived

def prints_numeric_header(blocks_number):
    for block in range(blocks_number+1):
        if (block)%4 == 0 and block !=0:
            print(str(block).rjust(4), end=' ')

    print()    

def prints_squares(years_to_live, blocks_number, blocks_lived):
    lived = "◼"
    unlived = "◻"
    
    for year in range(years_to_live):
        print(str(year).rjust(2), end = '  ')
        for block in range(blocks_number):
            if (block+1)%4 == 0 and block !=0:
                if blocks_lived > 0:
                    print(lived + " ", end='')
                    blocks_lived = blocks_lived - 1
                else:
                    print(unlived + " ", end='')
            else:
                if blocks_lived > 0:
                    print(lived, end='')
                    blocks_lived = blocks_lived - 1
                else:
                    print(unlived, end='')   
        print(" ")
        if (year+1)%10 == 0:
            print(" ")

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')