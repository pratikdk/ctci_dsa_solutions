import unittest

def unique(string):
    if len(string) > 128:
        return False

    charset_flag = [False for i in range(128)]

    for char in string:
        char_ord = ord(char)
        if charset_flag[char_ord]:
            return False
        charset_flag[char_ord] = True

    return True

class Test(unittest.TestCase):
    dataT = ["ghyu", "yuio"]
    dataF = ["aaab", "1ab1"]

    def test_for_unique(self):
        print("Running Test")
        # True check
        for t_string in self.dataT:
            actual = unique(t_string)
            self.assertTrue(actual)
        # False check
        for f_string in self.dataF:
            actual = unique(f_string)
            self.assertFalse(actual)
    

if __name__ == "__main__":
    unittest.main()
