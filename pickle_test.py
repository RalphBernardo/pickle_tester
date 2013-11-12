import unittest
from pickler import list_pickler, unpickler
from os import remove

class test_pickle(unittest.TestCase):

    def test_lists_equal_using_pickle(self):
        my_list = ['R', 'a', 'l', 'p', 'h']
        file_pickled = open('pickle_test.txt', 'w') #open file if exists, create it otherwise
        list_pickler(my_list, file_pickled)
        file_pickled.close()
        file_pickled = open('pickle_test.txt', 'r') #open file for reading
        unpickled_list = unpickler(file_pickled)
        file_pickled.close()
        remove('pickle_test.txt') #delete file
        self.assertEqual(my_list, unpickled_list)
