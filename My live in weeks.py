from mliw_functions import *

"""
A year has 52,143 weeks, 
so each block represents 1.00275 weeks.
week = 0.99725754176 block.
"""

if __name__ == "__main__":
    years_to_live = 70
    blocks = 52

    birth_date = input("Enter your birthdate(yyyy-mm-dd) : ")
    birth = birth_date_to_dic(birth_date)

    days_lived = return_days_lived(birth['year'], birth['month'], birth['day'])
    weeks_lived = int(days_lived/7)
    blocks_lived = int(weeks_lived/1.00275)

    clear_screen()

    print("MY LIFE IN WEEKS".center(68), end='\n\n    ')

    prints_numeric_header(blocks)

    prints_squares(years_to_live, blocks, blocks_lived)