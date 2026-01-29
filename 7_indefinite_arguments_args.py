def tea_order(customer_name, tea_type, milk = None, sweetner= None):
    print(customer_name, "ordered a" , tea_type, "tea")
    if milk!=None:
        print(" - Add:" , milk)
    if sweetner!= None:
        print(" - Add:" , sweetner)

    tea_order("Alice","Chamomile")
    tea_order("Bob", "black", "oat")
    tea_order("Tony", "black", "oat", "honey")


def tea_order(customer_name, tea_type, *args):
    print(customer_name, "ordered a" , tea_type, "tea")
    for arg in args:
        print("   - Add:", arg)


    tea_order("Alice","Chamomile")
    tea_order("Bob", "black", "oat")
    tea_order("Tony", "black", "oat", "honey")



def tea_order(customer_name, tea_type, **kwargs):
    print(customer_name, "ordered a" , tea_type, "tea")
    for key, value in kwargs.items():
        print("   -Add", key , ":", value)


    tea_order("Alice","Chamomile")
    tea_order("Bob", "black", milk="oat")
    tea_order("Tony", "black", milk="oat", sweetner="honey")



def tea_order(customer_name, tea_type, *args, **kwargs):
    print(customer_name, "ordered a" , tea_type, "tea")
    for arg in args:
        print("   - Add:", arg)

    for key, value in kwargs.items():
        print("   -Add", key , ":", value)


    tea_order("Alice","Chamomile")
    tea_order("Bob", "black", milk="oat")
    tea_order("Tony", "black", milk="oat", sweetner="honey")


def tea_order(customer_name, tea_type, *args, **kwargs):
    print(customer_name, "ordered a" , tea_type, "tea")
    for arg in args:
        print("   - Add:", arg)

    for key, value in kwargs.items():
        print("   -Add", key , ":", value)

        eves_extras =("milk": "almond", "sweetner": "sugar", "flavor": "lemon")
        tea_order("Eve","green", **eves_extras)








# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
def sum_squares(*args):
    total=0                # Initialize total to 0
    for num in args:       # Iterate through each arguement
        total += num ** 2  # Add the quare of the number to total
        # 
        #
        #


    return total # Retutn the total sum of squares
print(sum_squares(1,2,3)) # Example usage




# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total=0                # Initialize total to 0
    for num in args:       # Iterate through each arguement
        total += abs(num)  # Add the quare of the number to total
        # first time through loop: 0 + abs(-1)=1
        # second time through loop: 0 + abs(2)=3
        # third time through loop: 0 + abs(-3)=6
    return total
print(sum_squares(-1,2,-3)) # Example usage





# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.
def personal_numbers(*args):
    total=0
    for num in args:
        sum +- num
        print(f:{num}, the sum of your numbers is {sum_numbers})

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"