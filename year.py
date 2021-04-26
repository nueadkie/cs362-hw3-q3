# To run, enter into a terminal:
# python chris_miraflor_hw1.py
#
# Then, enter an integer as the input year. The software will then display if 
# the input would be a leap year or not.

year = input("Enter a year: ")
# Convert to int.
year = int(year)

# Check if the number is a leap year - 
# divisible by 4 and not divisible by 100 unless divisible by 400.
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
  print(year, "is a leap year.")
else:
  print(year, "is NOT a leap year.")