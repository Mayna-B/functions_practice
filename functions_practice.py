# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
    print("Hello!")

hello()

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(item1, item2, item3):
    packed_list = [item1, item2, item3]
    return packed_list

packed = pack("apple", "orange", "banana")
print(packed)  

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" 
# (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.
def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {food_list[0]}")
        for item in food_list[1:]:
            print(f"Next I eat {item}")

food_items = ["sandwich", "chips", "apple"]
eat_lunch(food_items)