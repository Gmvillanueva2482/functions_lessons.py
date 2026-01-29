# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

def all_positives(values):
    for v in values:
        if v < 0:
            return False
    return True

numbers = [3, -1, 7, 12, -5]





# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

def sum_less(numbers):
    total = 0
    for num in numbers:
        if 0 < num < 1000:
            total += num
    return total


numbers = [10, -5, 250, 1500, 999, 0, 42]

print(sum_less(numbers))





# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

numbers = [3, 8, 12, 7, 0, 25, 44]

print(count_even(numbers))  