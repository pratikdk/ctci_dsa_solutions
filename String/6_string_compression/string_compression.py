import unittest

def compress(string):
    compressed = []
    char_counter = 0

    for i, char in enumerate(string):
        char_counter += 1
        if ((i+1 >= len(string)) or (char != string[i+1])): # If its last char or curr char is not equal to next char
            compressed.append(char+str(char_counter))
            char_counter = 0 # reset counter
    compressed_string = "".join(compressed)
    return  compressed_string if len(compressed_string) < len(string) else string


class Test(unittest.TestCase):
    data = [
        ('aabbcccddddefzzzz', 'a2b2c3d4e1f1z4'),
        ('aabbccdd', 'aabbccdd'),
        ('abcd', 'abcd')
    ]

    def test_compression(self):
        for test_string, expected_string in self.data:
            result = compress(test_string)
            self.assertEqual(result, expected_string)

if __name__ == "__main__":
    unittest.main()
