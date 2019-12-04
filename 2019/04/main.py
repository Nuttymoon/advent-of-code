import os
from math import floor


def test_password(password):
    digits = str(password)
    following = False
    repeating = 1

    for i, d in enumerate(digits[1:]):
        if int(d) < int(digits[i]):
            return False

        if d == digits[i]:
            repeating += 1
        else:
            if repeating == 2:
                following = True

            repeating = 1

    if repeating == 2:
        following = True

    if following:
        return True
    else:
        return False


def get_possible_passwords(min_password, max_password):
    possible_passwords = []

    for password in range(min_password, max_password):
        if test_password(password):
            possible_passwords.append(password)

    return possible_passwords


if __name__ == '__main__':
    print('Number of possible passwords = ',
          len(get_possible_passwords(347312, 805915)))
