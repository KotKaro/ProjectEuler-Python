from typing import List


def multiply_last_items(numbers: List[int]) -> List[int]:
    for index in range(0, len(numbers)):
        end_index = len(numbers) - 1 - index
        if index >= end_index:
            return [number for number in numbers if number > 0]

        numbers[index] = numbers[index] * numbers[end_index]
        numbers[end_index] = 0


def get_factorial(number: int):
    numbers = [number for number in range(1, number + 1)]

    while len(numbers) > 1:
        numbers = multiply_last_items(numbers)

    return numbers[0]


def get_digits_sum_for_factorial(number: int):
    return sum([int(char) for char in str(get_factorial(number))])
