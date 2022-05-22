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
    total_not_zero = 0
    total_zero = 0

    to_calculate = [[index, zeros_count] for index in range(minimal_count_of_same_numbers, total_digits_count + 1) for
                    zeros_count in
                    range(1, minimal_count_of_same_numbers)]

    for index in range(minimal_count_of_same_numbers, total_digits_count + 1):
        total_not_zero_remaining = total_digits_count - index
        to_multiply = 1 if total_not_zero_remaining == 0 else 8 ** total_not_zero_remaining
        total_not_zero += 9 * get_placement_combinations(total_digits_count, index) * to_multiply

        if total_digits_count - 1 < index:
            continue

        zero_remaining_number = total_digits_count - index - 1
        to_multiply = 1 if zero_remaining_number <= 0 else 9 ** zero_remaining_number
        total_zero += 9 * get_placement_combinations(total_digits_count - 1, index) * to_multiply

        for zeros_count in range(1, minimal_count_of_same_numbers):
            if zeros_count + index > total_digits_count:
                continue

            zeros_placements = get_placement_combinations(total_digits_count - 1, zeros_count)
            non_zeros_placements = get_placement_combinations(total_digits_count - zeros_count,
                                                              index)
            other_numbers = total_digits_count - (index + zeros_count)
            to_multiply = 1 if other_numbers <= 0 else 8 ** other_numbers
            total += 9 * non_zeros_placements * zeros_placements * to_multiply

    return total + total_zero + total_not_zero


def count_of_dominating_numbers_to_power(power: int):
    all_powers = []
    powers = list(reversed(range(1, power + 1)))

    for power in powers:
        print("Calculating for: {0}".format(power))
        all_powers.append(count_of_dominating_numbers_in_power(power))

    return sum(all_powers)


if __name__ == '__main__':
    start_time = time.time()

    # wzor n!(n-k)!

    n = 2022
    comb = (int(n / 2) + 1) ** 10 * ((int(n / 2) - 1) ** 10)
    result = comb % 1_000_000_007;

    print("--- %s seconds ---" % (time.time() - start_time))
