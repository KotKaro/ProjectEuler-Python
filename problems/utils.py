def get_sum_of_dividers(number: int):
    return sum([divider for divider in range(1, int(number / 2) + 1) if number % divider == 0])