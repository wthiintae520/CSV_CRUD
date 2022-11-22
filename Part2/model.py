'''
Created on October 13, 2022
Modified on October 14, 2022
Description: This file control the sequential data structure
@author: Yunting Yin
'''

# in charge of the sequential data structure
class Data:
    
    # uses row values from csv file to build an object
    def __init__(self, source="", latin_name="", english_name="", french_name="", year="", month="", number_otoliths=""):
        self.set_source(source)
        self.set_latin_name(latin_name)
        self.set_english_name(english_name)
        self.set_french_name(french_name)
        self.set_year(year)
        self.set_month(month)
        self.set_number_otoliths(number_otoliths)

    # the string version of the Data object
    def __str__(self):
        txt = "{}, {}, {}, {}, {}, {}, {}\n"
        return txt.format(self.__source, self.__latin_name, self.__english_name, self.__french_name, self.__year, self.__month, self.__number_otoliths)

    # getters
    def get_source(self):
        return self.__source
    def get_latin_name(self):
        return self.__latin_name
    def get_english_name(self):
        return self.__english_name
    def get_french_name(self):
        return self.__french_name
    def get_year(self):
        return self.__year
    def get_month(self):
        return self.__month
    def get_number_otoliths(self):
        return self.__number_otoliths
    
    # setters
    def set_source(self, source):
        self.__source = source
    def set_latin_name(self, latin_name):
        self.__latin_name = latin_name
    def set_english_name(self, english_name):
        self.__english_name = english_name
    def set_french_name(self, french_name):
        self.__french_name = french_name
    def set_year(self, year):
        self.__year = year
    def set_month(self, month):
        self.__month = month
    def set_number_otoliths(self, number_otoliths):
        self.__number_otoliths = number_otoliths
