import random
from insertion_sort import insertion_sort
from merge_sort import merge_sort

def get_unordered_list(quantity):
    number_list = []
    for _ in range (quantity):
        number_list.append(random.randrange(1, quantity))
    print(number_list)

unordered_list = get_unordered_list(50)

def main():
    pass

if __name__=="__main__":
    main()