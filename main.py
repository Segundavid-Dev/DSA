# Interview Cake

myArray = ["david", "segun", "olasunkanmi"]

def print_first_item(item):
    print(item[0])



print_first_item(myArray)

# This algorithm runs in 0(1), constant time. The list could be 1 or 1000 items, but this function would only require one step

def print_all_item(item):
    for i in item:
        print(i)


print_all_item(myArray)
# This algorithm runs in 0(n), linear time where n is the number of items in the list,
# if the item is 10, we have

# Another type of algorithm
def say_hi_n_times(n):
    for time in range(n):
        print("hii")