import unittest

def is_palindrome_permutation(string):
    bit_vector = construct_bit_vector(string)
    return (bit_vector == 0) | check_exactly_one_bit_set(bit_vector) # one extra char is allowed


def construct_bit_vector(string):
    bit_vector = 0
    for char in string:
        char_position = get_char_number(char)
        bit_vector = toggle(bit_vector, char_position)
    return bit_vector


def toggle(bit_vector, char_position):
    if (char_position < 0):
        return bit_vector
    mask = 1 << char_position # Shift one by about char_position to the left
    if (bit_vector & mask) == 0: # if not Already activated bit
        bit_vector |= mask # toggle up # Activate it
    else:
        bit_vector &= ~mask # reset down
    return bit_vector


def check_exactly_one_bit_set(bit_vector):
    return (bit_vector & (bit_vector - 1)) == 0


def get_char_number(char):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    c = ord(char)

    if a <= c <= z:
        return c - a
    elif A <= c <= Z:
        return c - A
    return -1


class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('Pratik kitarp', True),
        ('azAZ', True),
        ('random string', False)
    ]

    def test_permutation(self):
        for test_string, expected in self.data:
            result = is_palindrome_permutation(test_string)
            self.assertEqual(result, expected)

    print("Test Passed!")

if __name__ == "__main__":
    unittest.main()
