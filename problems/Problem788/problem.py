import math
import time


def is_dominating_number(number: int):
    string_number = str(number)
    string_number_half_length = len(string_number) / 2
    keys_dictionary = {}
    for char in string_number:
        if char in keys_dictionary:
            keys_dictionary[char] = keys_dictionary[char] + 1
        else:
            keys_dictionary[char] = 1
        if keys_dictionary[char] > string_number_half_length:
            return True

    return False


def get_placement_combinations(available_places: int, places_to_fill: int) -> int:
    # possible placement combinations
    # n - possible ways
    # p - places to fill
    # n!/p!(n-p)!
    return math.factorial(available_places) / (math.factorial(places_to_fill) * math.factorial(
        available_places - places_to_fill))


def count_of_dominating_numbers_in_power(power: int):
    total = 0
    total_digits_count = power
    minimal_count_of_same_numbers = int((total_digits_count / 2)) + 1
    remaining_number = total_digits_count - minimal_count_of_same_numbers

    # combinations without zero
    total += get_placement_combinations(total_digits_count, minimal_count_of_same_numbers) * 9 * 9**remaining_number

    # combinations with zero
    if remaining_number - 1 >= 0:
        total += 9 * (get_placement_combinations(total_digits_count - 1, minimal_count_of_same_numbers) * 10 ** (remaining_number - 1))

    return total


def count_of_dominating_numbers_to_power(power: int):
    total = 0
    for power in range(1, power + 1):
        total += count_of_dominating_numbers_in_power(power)

    return total


def count_of_dominating_numbers_to_power_slow(power: int):
    total = 0
    for number in range(1, 10 ** power):
        if is_dominating_number(number):
            print(number)
            total += 1

    return total


def count_of_dominating_numbers_in_power_slow(power: int):
    total = 0
    for number in range(10 ** (power - 1), 10 ** power):
        if is_dominating_number(number):
            print(number)
            total += 1

    return total


if __name__ == '__main__':
    start_time = time.time()

    # wzor n!(n-k)!

    n = 2022
    comb = (int(n / 2) + 1) ** 10 * ((int(n / 2) - 1) ** 10)
    result = comb % 1_000_000_007;

    print("--- %s seconds ---" % (time.time() - start_time))
