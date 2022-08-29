def update_order(new_item, current_order=[]):
    current_order.append(new_item)
    return current_order

# First order, burger
order1 = update_order({'item': 'burger', 'cost': '3.50'})

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2) # [{'item': 'burger', 'cost': '3.50'}, {'item': 'soda', 'cost': '1.50'}]

# Default parameter values are evaluated from left to right when the function
# definition is executed. This means that the expression is evaluated once, when
# the function is defined, and that the same “pre-computed” value is used for
# each call.
# This means current_order=[] was only created once and anytime we tried to
# access it, the same list was being modified since is a mutable object we can
# modify it.

# We can even see that the memory id is the same for both orders.
print(id(order1))
print(id(order2))

# The None Workaround
def create_student(name, age, grades=None):
    # Will help us to created a new empty list each time this function is called.
    if grades is None:
        grades = []
    return {
        'name': name,
        'age': age,
        'grades': grades
    }

def add_grade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])

chrisley = create_student('Chrisley', 15)
dallas = create_student('Dallas', 16)

add_grade(chrisley, 90)
add_grade(dallas, 100)
