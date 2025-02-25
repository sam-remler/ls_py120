str1 = "I'm a string"
str2 = "I'm a string"

print(not(str1 > str2))

try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    result = num1 / num2
except ZeroDivisionError:
    print('Cannot divide by zero!')
except ValueError:
    print('Please enter valid numbers!')
else:
    print(f'The result is: {result}')
finally:
    print('End of program')


try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    result = num1 / num2
except (ZeroDivisionError,ValueError) as e:
    print(e)
else:
    print(f'The result is: {result}')
finally:
    print('End of program')



num = float(input("Enter a positive number: "))
if num < 0:
    raise ValueError("Must be positive integer")


class NegativeNumberError(ValueError):
    pass

num = float(input('Enter a number: '))
if num < 0:
    raise NegativeNumberError('Negative numbers are not allowed!')
print(f'You entered {num}')


def invert_list_of_numbers(lst : list):
    new_lst = []
    for num in lst:
        try:
            new_num = (1 / num)
            new_lst.append(new_num)
        except ZeroDivisionError as e:
            new_lst.append(float('inf'))


students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    try:
        return students[name]
    except KeyError:
        return 'Student Not Found'
    

numbers = [1, 2, 3, 4, 5]

def sixth_element(nums):
    if len(numbers) > 5:
        return None
    else:
        return nums[5]

def sixth_element(nums):
    try:
        return nums[5]
    except IndexError:
        return None

str1 = "I'm a string"
str2 = "I'm a string"

print(not(str1 > str2))