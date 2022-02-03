from math import *
import timeit

print("Welcome to prime calculator!")
range_or_single = input("Would you like to test a range of numbers of a single number? (Range/Single): ")

if range_or_single == "Range":
    lower_number = input("What is the START of the range you would like to test?: ")
    upper_number = input("What is the END of the range you would like to test?: ")
    range_of_numbers = list(range(int(lower_number), int(upper_number) + 1))
elif range_or_single == "Single":
    single_number = input("What is your single number: ")
    range_of_numbers = list(range(int(single_number), int(single_number) + 1))
else:
    print("Error rerun script")
    exit()

start = timeit.default_timer()
for number in range_of_numbers:
    small_list = list(range(2,number))
    b=[]
    for i in small_list:
        a = number % i
        b.append(a)
    if range_or_single == "Single" and 0 in b:
        print(str(number) + " is not a Prime!")
    if 0 not in b:
        print(str(number) + " is a Prime!")


print("Thank you for selecting the Tyson Prime Calculator.")
stop = timeit.default_timer()
execution_time = stop - start

print("You just tested " + str(len(range_of_numbers)) + " numbers for primes in a mere " + str(round(execution_time, 2)) + " seconds!!")

