#   Filename:           Lab 2
#   Created by:         jasongreen
#   Date:               Saturday, January 19, 2019
#   Time of Creation:   11:14
#   ---

# average of 50 salaries
def salary_sum(number_list):
    total_Sum = 0
    for i in number_list:
        total_Sum = total_Sum + i
    return total_Sum / i


# this array is used as an example of 50 salaries,
# increasing from $1 to $50 as an example. In
# reality, I would be pulling from an SQL database.
print(salary_sum([1,2,3,4,5,6,7,8,9,
                  10,11,12,13,14,15,16,17,18,19,
                  20,21,22,23,24,25,26,27,28,29,
                  30,31,32,33,34,35,36,37,38,39,
                  40,41,42,43,44,45,46,47,48,49,
                  50]))






# print largest number out of three

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a number: "))
number3 = int(input("Please enter a number: "))
largest = -1e10

if (number1 > number2) and (number1 > number3):
    largest = number1
elif (number2 > number1) and (number2 > number3):
    largest = number2
else:
    largest = number3

print(largest)




# ordering paper boxes and printing copies of the board meeting
# report given the number of pages in the report, the number of
# meeting attendees, and the number of papers per paper box. You
# can only order whole boxes. You need to print five extra copies.

import math

n_reps = 100
n_extra_reps = 25
n_pages = 20
n_papers_box = 200
n_req_papers = (n_reps + n_extra_reps) * n_pages
n_req_boxes = math.ceil(n_req_papers / n_papers_box)

print("The number of required paper boxes = {0}".format(n_req_boxes))























