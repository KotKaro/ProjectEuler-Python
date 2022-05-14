single = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
toTwenty = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def parse_number_to_word(number: int) -> str:
    if number < 10:
        return single[number]
    if number == 10:
        return tens[0]
    if number < 20:
        return toTwenty[number - 11]
    if number < 100:
        first_part = tens[int(str(number)[0]) - 1]
        second_part = parse_number_to_word(int(str(number)[1]))
        return '{0} {1}'.format(first_part, second_part)
    if number < 1000:
        first_part = int(str(number)[0])
        second_part = int(str(number)[1:])
        if second_part > 0:
            return '{0} hundred and {1}'.format(parse_number_to_word(first_part), parse_number_to_word(second_part))
        else:
            return '{0} hundred'.format(parse_number_to_word(first_part))
    if number < 10000:
        first_part = int(str(number)[0])
        return '{0} thousand {1}'.format(parse_number_to_word(first_part), parse_number_to_word(int(str(number)[1:])))


def get_letters_count_in_range_without_spaces(start: int, stop: int) -> int:
    if start > stop:
        raise ValueError('Start number cannot be grater than stop')

    letters_sum = 0
    for x in range(start, stop + 1):
        to_count = parse_number_to_word(x).replace(' ', '')
        letters_sum += len(to_count)
        print('{0}-and sum is:{1}'.format(to_count, letters_sum))

    return letters_sum
