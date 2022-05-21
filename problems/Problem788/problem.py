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

    total_not_zero = 0
    for index in range(minimal_count_of_same_numbers, total_digits_count + 1):
        total_not_zero_remaining = total_digits_count - index
        to_multiply = 1 if total_not_zero_remaining == 0 else 8 ** total_not_zero_remaining
        total_not_zero += 9 * get_placement_combinations(total_digits_count, index) * to_multiply

    total_zero = 0
    for index in range(minimal_count_of_same_numbers, total_digits_count):
        zero_remaining_number = total_digits_count - index - 1
        to_multiply = 1 if zero_remaining_number <= 0 else 9 ** zero_remaining_number
        total_zero += 9 * get_placement_combinations(total_digits_count - 1, index) * to_multiply

    for count_of_zeros in range(1, minimal_count_of_same_numbers):
        for minimal_count_of_same in range(minimal_count_of_same_numbers, total_digits_count):
            if count_of_zeros + minimal_count_of_same > total_digits_count:
                continue

            zeros_placements = get_placement_combinations(total_digits_count - 1, count_of_zeros)
            non_zeros_placements = get_placement_combinations(total_digits_count - count_of_zeros, minimal_count_of_same)
            other_numbers = total_digits_count - (minimal_count_of_same + count_of_zeros)
            to_multiply = 1 if other_numbers <= 0 else 8 ** other_numbers
            total += 9 * non_zeros_placements * zeros_placements * to_multiply


    return total + total_zero + total_not_zero


def count_of_dominating_numbers_to_power(power: int):
    all_powers = []
    for power in range(1, power + 1):
        print("Calculating for: {0}".format(power))
        all_powers.append(count_of_dominating_numbers_in_power(power))

    return sum(all_powers)


def count_of_dominating_numbers_to_power_slow(power: int, digit_to_replace: int = None, times: int = None):
    total = 0
    for number in range(10**(power - 1), 10 ** power):
        if is_dominating_number(number):
            if digit_to_replace is not None and times is not None:
                if len(str(number)) - len(str(number).replace(str(digit_to_replace), '')) == times:
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
