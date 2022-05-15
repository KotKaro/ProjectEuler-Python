from typing import List

from problems.utils import get_sum_of_dividers


def get_amicable_numbers_in_range(start: int, stop: int) -> List[int]:
    for number in range(start, stop):
        sum_of_number_dividers = get_sum_of_dividers(number)
        sum_of_dividers_of_number_sum_of_dividers = get_sum_of_dividers(sum_of_number_dividers)
        if sum_of_dividers_of_number_sum_of_dividers == number \
                and sum_of_number_dividers != sum_of_dividers_of_number_sum_of_dividers:
            yield number


def get_sum_of_amicable_numbers_in_range(start: int, stop: int):
    return sum(list(get_amicable_numbers_in_range(start, stop)))
