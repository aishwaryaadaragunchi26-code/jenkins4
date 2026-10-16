
import sys

def leapYear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

if __name__ == "__main__":
    year = int(sys.argv[1])
    print(leapYear(year))