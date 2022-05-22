import math
import time


def get_placement_combinations(available_places: int, places_to_fill: int) -> int:
    # possible placement combinations
    # n - possible ways
    # p - places to fill
    # n!/p!(n-p)!
    return math.factorial(available_places) // (math.factorial(places_to_fill) * math.factorial(
        available_places - places_to_fill))


def count_of_dominating_numbers_in_power(power: int):
    total_digits_count = power
    minimal_count_of_same_numbers = int((total_digits_count / 2)) + 1

    total = 0

    for index in range(minimal_count_of_same_numbers, total_digits_count + 1):
        total_not_zero_remaining = total_digits_count - index
        to_multiply = 1 if total_not_zero_remaining == 0 else 9 ** total_not_zero_remaining
        total += 9 * get_placement_combinations(total_digits_count, index) * to_multiply

    return total


def count_of_dominating_numbers_to_power(power: int):
    all_powers = []
    powers = list(reversed(range(1, power + 1)))
    for power in powers:
        start_time = time.time()
        print("Calculating for: {0}".format(power))
        all_powers.append(count_of_dominating_numbers_in_power(power))
        print("--- %s seconds ---" % (time.time() - start_time))
    return sum(all_powers)
