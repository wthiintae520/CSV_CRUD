'''
Created on October 14, 2022
Modified on October 14, 2022
Description: This file control the File-IO
@author: Yunting Yin
'''
import unittest
import model

class Test(unittest.TestCase):

    # test the getter and setter of source
    def test_source_getter_and_setter(self):
        data_object = model.Data()
        data_object.set_source("Taiwan")
        testString = format(data_object.get_source())
        self.assertEqual(testString, "Taiwan")

if __name__ == "__main__":
    unittest.main()
