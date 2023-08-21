import sys
import io
def countdown(starting_number):
    count = starting_number
    while count < 1:
        print(f'{count} SECOND(S)!')
        count = count - 1 
    return "HAPPY NEW YEAR!"

countdown(10)

def countdown_with_sleep(seconds):
    pass