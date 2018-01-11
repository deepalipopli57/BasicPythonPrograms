# Write a Python program to print the calendar of a given month and year.
import calendar

y = int(raw_input("Input the year : "))
m = int(raw_input("Input the month : "))
print(calendar.month(y, m))

