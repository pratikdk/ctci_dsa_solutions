import unittest

def is_unique(string):
    checker = 0
    for char in string:
        char_ord = ord(char) # ord(char) - ord('a')
        if (checker & (1 << char_ord)) > 0:
            return False
        checker |= (1 << char_ord)
    return True


class Test(unittest.TestCase):
    dataT = ["ghyu", "yuio"]
    dataF = ["aaab", "drtt"]

    def test_for_unique(self):
        print("Running Test")
        # True check
        for t_string in self.dataT:
            actual = is_unique(t_string)
            self.assertTrue(actual)
        # False check
        for f_string in self.dataF:
            actual = is_unique(f_string)
            self.assertFalse(actual)
    print("Test Passed!")

if __name__ == "__main__":
    unittest.main()
