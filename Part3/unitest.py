"""
Created on November 17, 2022
Modified on November 17, 2022
Description: This file control the File-IO
@author: Yunting Yin
"""
import unittest
import otolith

class Test(unittest.TestCase):

    # test the overridden __str__ method in otlith.py
    def test_otlith_string_method(self):
        my_otolith = otolith.Otolith("Dajia River", "Oncorhynchus masou", "Formasan landlocked salmon", "Ouananiche de Formose", "2022", "10", "9")
        test_string = my_otolith.__str__()
        self.assertEqual(test_string, "Dajia River, Oncorhynchus masou, Formasan landlocked salmon, Ouananiche de Formose, 2022, 10, 9\n")

if __name__ == "__main__":
    unittest.main()
