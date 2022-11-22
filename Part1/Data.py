''' 
Author: Yunting Yin
Date: September 22, 2022
Modified September 22, 2022
Description: This program uses Python inbuilt open function to read a CSV file.
Record the column values for each row to a record object, add that object to an array and
the display the values on the console. 
Also print records from the CSV dataset on screen.
'''

class RecordObject:
    '''
    uses row values from csv file to build an object
    '''
    def __init__(self, source="", latin_name="", english_name="", french_name="", year="", month="", number_otoliths=""):
        self.set_source(source)
        self.set_latin_name(latin_name)
        self.set_english_name(english_name)
        self.set_french_name(french_name)
        self.set_year(year)
        self.set_month(month)
        self.set_number_otoliths(number_otoliths)

    '''
    getters
    '''
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
    
    '''
    setters
    '''
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


#Author: Yunting Yin
#Open NAFO-4TVN-Atlantic-Cod-otoliths.csv and return a stream and set it to csvfile
try:
    csvfile = open("NAFO-4TVN-Atlantic-Cod-otoliths.csv", "r")
except Exception as e:
    print("NAFO-4TVN-Atlantic-Cod-otoliths.csv file not found")

dataset = []
#Reading the first 10 lines of file
for i in range(10):
    line = csvfile.readline()
    elements = line.split(",")
    #create the record object
    obj = RecordObject()
    #set the values from the csv to the record object
    obj.set_source(elements[0][1:-1])
    obj.set_latin_name(elements[1][1:-1])
    obj.set_english_name(elements[2][1:-1])
    obj.set_french_name(elements[3][1:-1])
    obj.set_year(elements[4])
    obj.set_month(elements[5])
    obj.set_number_otoliths(elements[6])
    
    #add the record object to the array
    dataset.append(obj)
    
#Print name
print("Name: Yunting Yin")
#Print column
print("{:^13} {:^13} {:^13} {:^13} {:^7} {:^7}".format("source", "latin_name", "english_name", "french_name", 
        "year", "month", "number_otoliths"))
#Printing the dataset
for i in range(1, 10):
    print("{:^13} {:^13} {:^13} {:^13} {:^7} {:^7}".format(dataset[i].get_source(), dataset[i].get_latin_name(),
        dataset[i].get_english_name(), dataset[i].get_french_name(), dataset[i].get_year(), dataset[i].get_month(),
        dataset[i].get_number_otoliths()))