import random
import string


def random_strings(length, num):
    strings = []
    while len(strings) < num:
        r_string = "".join(random.choice(string.ascii_lowercase) for i in range(length))
        if r_string not in strings:
            strings.append(r_string)
    return strings


# print(random_strings(2, 24))
