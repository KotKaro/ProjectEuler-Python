import time


def generate_permutations(array_to_alter, current_result: str = ''):
    for zero in array_to_alter:
        to_return = current_result + zero

        altered_array = list(array_to_alter)
        altered_array.remove(zero)

        if len(altered_array) == 0:
            yield to_return

        for permutation in generate_permutations(altered_array, to_return):
            yield permutation


def get_nth_permutation(array_to_alter, number: int):
    index = 0
    for permutation in generate_permutations(array_to_alter):
        index += 1
        if index == number:
            return permutation


if __name__ == '__main__':
    start_time = time.time()
    result = get_nth_permutation(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 100_000_0)
    print(result)
    print("--- %s seconds ---" % (time.time() - start_time))
