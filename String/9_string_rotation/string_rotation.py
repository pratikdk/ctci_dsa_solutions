import unittest

def is_substring(string, sub):
    return string.find(sub) != -1

def string_rotation(s1, s2):
    if (len(s1) == len(s2)) and len(s1) > 0:
        return is_substring(s1+s1, s2)
    else:
        return False

class Test(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('pratik', 'atikpr', True),
        ('random', 'string', False)
    ]

    def test_string_rotation(self):
        for s1, s2, expected in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
