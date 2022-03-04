# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def get_stat():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(n_student):
        grade_list.append(int(input('Enter a number: ')))

    # Calculate the mean and standard deviation of the grades
    sum_of_grades = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum_of_grades += grade
    mean = sum_of_grades / len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    standard_deviation = math.sqrt(sum_of_sqrs / len(grade_list))
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(standard_deviation, 3))

def print_stat():
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    get_stat()
    print('****** END ******')

print_stat()
