import unittest

def is_palindrome_permutation(string):
    odd_count = 0

    alphaset_counts = [0 for _ in range(ord('z') - ord('a') + 1)]

    for char in string:
        char_position = get_char_number(char)
        if char_position != -1:
            alphaset_counts[char_position] += 1
            if alphaset_counts[char_position] % 2 == 0: # odd == 1+
                odd_count -= 1
            else: # even
                odd_count += 1
    return odd_count <= 1 # 1 for odd string size


def get_char_number(char):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    c = ord(char)

    if a <= c <= z:
        return c - a
    elif A <= c <= z:
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
