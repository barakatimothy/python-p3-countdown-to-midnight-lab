import sys
import io
import time
def countdown(number):
    for i in range(number, 0, -1):
        print(f"{i} SECOND(S)!")
    print("HAPPY NEW YEAR!")

countdown(10)


def countdown_with_sleep(number):
    for i in range(number, 0, -1):
        print(f"{i} SECOND(S)!")
        time.sleep(1)  # Sleep for 1 second
    print("HAPPY NEW YEAR!")


countdown_with_sleep(10)
    