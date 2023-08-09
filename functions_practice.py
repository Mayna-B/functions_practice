def hello():
    print("Hello!")

hello()


def pack(item1, item2, item3):
    packed_list = [item1, item2, item3]
    return packed_list

packed = pack("apple", "orange", "banana")
print(packed)  


def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {food_list[0]}")
        for item in food_list[1:]:
            print(f"Next I eat {item}")

food_items = ["sandwich", "chips", "apple"]
eat_lunch(food_items)