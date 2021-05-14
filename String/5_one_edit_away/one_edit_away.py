# import unittest
#
# def is_one_edit_away(s1, s2):
#     if len(s1) == len(s2):
#         return one_edit_replace(s1, s2)
#     elif len(s1)+1 == len(s2):
#         return one_edit_insert(s1, s2) # insert into s1
#     elif len(s1)-1 == len(s2):
#         return one_edit_insert(s2, s1) # insert into s2
#     else:
#         return False
#
#
# def one_edit_replace(a, b):
#     edited = False
#     for c1, c2 in zip(a,b):
#         if c1 != c2:
#             if edited: # Facilitate for 1 edit
#                 return False
#             edited = True
#     return True
#
#
# def one_edit_insert(a, b):
#     index_a = 0
#     index_b = 0
#     while (index_a < len(a)) & (index_b < len(b)): # terminates when shorter string runs out of length
#         if a[index_a] != b[index_b]:
#             # initially both indexes will be the same, but will  with one edit
#             if index_a != index_b:
#                 return False
#             index_b += 1
#         else:
#             index_a += 1
#             index_b += 1
#     return True


def is_one_edit(str1, str2):
    s1_len = len(str1)
    s2_len = len(str2)

    i = 0
    j = 0

    edit_count = 0

    while (i < s1_len and j < s2_len): #and (i != s1_len and j != s2_len):
        #print(i, j)
        if str1[i] != str2[j]:
            if s1_len < s2_len:
                j += 1
            elif s2_len < s1_len:
                i += 1
            else:
                i += 1
                j += 1
            edit_count += 1
        else:
            i += 1
            j += 1
        #print(">>", i, j)
    edit_count += s1_len - i
    edit_count += s2_len - j

    return edit_count

#print(is_one_edit('pdoraledor', 'ple'))
print(is_one_edit('pale', 'ple'))
print(is_one_edit('pdorale', 'ple'))
print(is_one_edit('paledor', 'ple'))

# class Test(unittest.TestCase):
#     data = [
#         ('pdoraledor', 'ple', True),
#         ('pales', 'pale', True),
#         ('pale', 'bale', True),
#         ('pale', 'bae', False),
#         ('zale', 'alez', False)
#     ]
#
#     def test_one_edit_away(self):
#         for test_string_a, test_string_b, expected in self.data:
#             result = is_one_edit_away(test_string_a, test_string_b)
#             self.assertEqual(result, expected)
#
#         print("Test Complete")
#
# if __name__ == "__main__":
#     unittest.main()
