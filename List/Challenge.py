my_list = [1 ,3 ,-2, 4, 7]

def remove_even(lst):
    odds = []
    for i in lst:
        if i % 2 != 0:
            odds.append(i)
    return odds
    

odd_integers = remove_even(my_list)
print(odd_integers)