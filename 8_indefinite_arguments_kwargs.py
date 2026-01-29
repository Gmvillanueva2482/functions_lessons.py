
# Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.

def number_attributes (**kwargs):
    return len(kwargs)


# Example 1: No arguments
print(number_attributes())  # Output: 0
# Example 2: Three arguments
print(number_attributes(name="Alice", age=30, city="New York"))  # Output: 3
# Example 3: Different types of arguments
print(number_attributes(a=1, b=[1, 2, 3], c={"key": "value"}))  # Output: 3




# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.

def list_attributes(**kwargs):
    return list(kwargs.values())

result1 = list_attributes(a=1, b=2, c=3)
print(result1)  # Output: [1, 2, 3]

result2 = list_attributes(name="Alice", age=30, role="Engineer")
print(result2)  # Output: ['Alice', 30, 'Engineer']

result3 = list_attributes()
print(result3)  # Output: [] (handles no arguments)








# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:

# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Ash", eye_color="brown", hair_color="black")

# Will print to the screen:

# Characteristics of Ash:
# eye_color: brown
# hair_color: black