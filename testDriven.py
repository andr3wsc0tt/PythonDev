# Filter Exec Format Lambda
import math
from random import randint, seed


def create_weird_hash():

    commands = [int, float, math.sqrt, hash, bin]

    selected_command = commands[randint(0, 4)]

    b = selected_command(randint(0, 99999))

    return b


def get_test_values():
    complexity = 5

    Range1 = randint(0, complexity)

    huge_range = [create_weird_hash() for i in range(Range1)]

    return huge_range


# create list of transformation commands (str, int, float, sqrt, hash, bin, 64, etc...)
# choose a number randomly and select that command
# execute that command on a randomly selected range [0 - 500000, a - a73mdd&3hg 038d_jL*HDK8]

def is_odd(n):
    return n % 2 != 0


def is_even(n):
    return n % 2 == 0


def hash_me(n):
    if isinstance(n, str):
        a = int(n, 2)
        return hash(a)
    return(hash(n))


def use_me():
    # While Time Remaining...
    test_values = get_test_values()

    # Use lambda to return hash and check for odd/even/prime/perfect numbers.
    # Filter find sum of hash, of individual strings that == True ( have hash values that are (odd: even: prime: perfect))

    # map hash -> then filter odd -> add to simple filtered

    simple_filtered = [i for i in list(
        filter(lambda x: x % 2 != 0, list(
            map(hash_me, test_values))))]

    radius = sum(simple_filtered) % 100
    print(radius)

    # the int value modded between (0-100) that are (odd : even: prime: perfect)
    # Print out the result of the command (if exists) in the center of a circle with radius returned from commmand: command will always return a (int: float: double)

    print(simple_filtered)


use_me()
