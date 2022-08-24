import os
from mliw_functions import *

"""
1984-11-23
a year has 52,143 weeks, 
so each block represents 1.00275 weeks.
week = 0.99725754176 block.
"""

years_to_live = 70
blocks = 52
lived = "◼"
unlived = "◻"

birth_date = input("Enter your birthdate(yyyy-mm-dd) : ")
birth = birth_date_to_dic(birth_date)

days_lived = days_lived(birth['year'], birth['month'], birth['day'])
weeks_lived = int(days_lived/7)
blocks_lived = int(weeks_lived/1.00275)
print(blocks_lived)
os.system('clear')

print("MY LIFE IN WEEKS".center(68), end='\n\n    ')

for block in range(blocks+1):
    if (block)%4 == 0 and block !=0:
        print(str(block).rjust(4), end=' ')

print()

for year in range(years_to_live):
    print(str(year).rjust(2), end = '  ')
    for block in range(blocks):
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
