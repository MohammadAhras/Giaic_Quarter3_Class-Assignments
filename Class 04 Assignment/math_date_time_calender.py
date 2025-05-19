import datetime
import calendar
import math

# Math Functions
print("🔢 Math Functions")
print("Square Root of 16:", math.sqrt(16))
print("2 to the power 5:", math.pow(2, 5))
print("Floor of 7.8:", math.floor(7.8))
print("Ceil of 7.2:", math.ceil(7.2))
print("Factorial of 5:", math.factorial(5))

# Date & Time
today = datetime.datetime.now()
future_date = today + datetime.timedelta(days=7)

print("\n📆 Date & Time")
print("Current Date & Time:", today.strftime("%Y-%m-%d %H:%M:%S"))
print("Date after 7 days:", future_date.strftime("%Y-%m-%d"))

# Calendar
year = int(input("\nEnter a year to check its calendar: "))
month = today.month

print(f"\n📅 Calendar for {calendar.month_name[month]} {year}")
print(calendar.month(year, month))

# Leap Year Check
print(f"{year} is a leap year." if calendar.isleap(year) else f"{year} is not a leap year.")
