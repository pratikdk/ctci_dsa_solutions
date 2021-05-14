import unittest

def urlify(char_list, length):
    max_index = len(char_list)

    for i in reversed(range(length)):
        print(i, char_list[i])
        if char_list[i] == ' ':
            char_list[max_index-3: max_index] = '%20'
            max_index -= 3
        else:
            char_list[max_index-1] = char_list[i]
            max_index -= 1

    return char_list

class Test(unittest.TestCase):
    data = [
        (list('A random string to test.        '), 24,
        list('A%20random%20string%20to%20test.')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))
    ]

    def test_urlify(self):
        for input_char_list, length, result in self.data:
            output_char_list = urlify(input_char_list, length)
            self.assertEqual(output_char_list, result)

    print("Test Passed!")

if __name__ == "__main__":
    unittest.main()
