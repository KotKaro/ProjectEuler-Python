import time

from problems.utils import get_sum_of_dividers

if __name__ == '__main__':
    start_time = time.time()
    abundant_numbers = [number for number in range(1, 28123) if get_sum_of_dividers(number) > number]
    abundant_sums = [x0 + y0 for x0 in abundant_numbers for y0 in abundant_numbers]
    result = sum(set(range(1, 28123)) - set(abundant_sums))
    print(result)
    print("--- %s seconds ---" % (time.time() - start_time))
