import unittest

def is_one_edit_away(s1, s2):
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1)+1 == len(s2):
        return one_edit_insert(s1, s2) # insert into s1
    elif len(s1)-1 == len(s2):
        return one_edit_insert(s2, s1) # insert into s2
    else:
        return False


def one_edit_replace(a, b):
    edited = False
    for c1, c2 in zip(a,b):
        if c1 != c2:
            if edited: # Facilitate for 1 edit
                return False
            edited = True
    return True


def one_edit_insert(a, b):
    index_a = 0
    index_b = 0
    while (index_a < len(a)) & (index_b < len(b)): # terminates when shorter string runs out of length
        if a[index_a] != b[index_b]:
            # initially both indexes will be the same, but will  with one edit
            if index_a != index_b:
                return False
            index_b += 1
        else:
            index_a += 1
            index_b += 1
    return True


class Test(unittest.TestCase):
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bae', False)
    ]

    def test_one_edit_away(self):
        for test_string_a, test_string_b, expected in self.data:
            result = is_one_edit_away(test_string_a, test_string_b)
            self.assertEqual(result, expected)

        print("Test Complete")

if __name__ == "__main__":
    unittest.main()
