def calculate_value_for_str(value: str, index: int):
    index_of_first_upper_char_in_ascii_table = 65
    value_to_match_natural_order_in_alphabet = 1
    return sum(
        [(ord(char) - index_of_first_upper_char_in_ascii_table) + value_to_match_natural_order_in_alphabet for char in
         value.upper()]) * index


if __name__ == '__main__':
    text = open('p022_names.txt', 'r').read()
    sorted_names = sorted([text[1:-1] for text in text.split(',')])
    result = sum([calculate_value_for_str(sorted_names[index], index + 1) for index in range(0, len(sorted_names))])
    print(result)
