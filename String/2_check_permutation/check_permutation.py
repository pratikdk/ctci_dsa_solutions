import unittest

def check_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False

    char_counts = [0 for i in range(128)]

    for char_a in string_a:
        char_ord = ord(char_a)
        char_counts[char_ord] += 1

    for char_b in string_b:
        char_ord = ord(char_b)
        char_counts[char_ord] -= 1
        if char_counts[char_ord] < 0:
            return False

    return True

class Test(unittest.TestCase):
    dataT = [
        ("abcd", "dcba"),
        ("1235", "3521"),
        ("!=()", "(!=)")
    ]
    dataF = [
        ("ab ", "abcd"),
        ("1234", "42133")
    ]
    def test_run(self):
        for test_tup in self.dataT:
            result = check_permutation(*test_tup)
            self.assertTrue(result)
        for test_tup in self.dataF:
            result = check_permutation(*test_tup)
            self.assertFalse(result)

    print("Test Passed!")


if __name__ == "__main__":
    unittest.main()
