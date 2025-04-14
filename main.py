import random
import timeit
from insertion_sort import insertion_sort
from merge_sort import merge_sort

quantity = [10, 100, 1_000, 10_000, 20_000]

def get_unordered_list(quantity):
    return [random.randrange(1, quantity) for _ in range (quantity)]

def run_test(sort_func, label):
    print(f"\n{label}")
    for size in quantity:
        lst = get_unordered_list(size)
        def wrapper():
            sort_func(lst.copy())
        time_taken = timeit.timeit(wrapper, number=1)
        print(f"Size {size:7d}: {time_taken:.7f} sec")

def main():
    run_test(insertion_sort, "Insertion sort")
    run_test(merge_sort, "Merge sort")
    run_test(lambda lst: lst.sort(), "Sort method sort")
    run_test(sorted, "Sorted method sort")
    
if __name__=="__main__":
    main()