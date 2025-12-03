import os
from math import floor


STARTING_POSITION = 50


def get_input_ranges():
    with open(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    ) as input_file:
        return list(filter(None, input_file.read().split(",")))


def read_range(range_string):
    start, end = range_string.split("-")

    return int(start), int(end)


def find_invalid_ids(range_start, range_end):
    invalid_ids = []
    for i in range(range_start, range_end + 1):
        id_string = str(i)
        id_string_middle = len(id_string) // 2

        for l in range(1, id_string_middle + 1):
            pattern = id_string[:l]
            if id_string.replace(pattern, "") == "":
                invalid_ids.append(i)
                break

    return invalid_ids


if __name__ == "__main__":
    invalid_ids_sum = 0

    for r in get_input_ranges():
        start, end = read_range(r)
        invalid_ids = find_invalid_ids(start, end)
        invalid_ids_sum += sum(invalid_ids)

        print(f"{start} - {end} -> {invalid_ids}")

    print(f"Invalid IDs sum: {invalid_ids_sum}")
