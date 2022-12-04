"""
Created on October 13, 2022
Modified on December 2, 2022
Description: This file control the File-IO
@author: Yunting Yin
"""
import matplotlib.pyplot as pl
import numpy as np
import otolith

# in charge of the File-IO
class Controller:

    # reload the dataset
    def reload(self):
        Controller.print_name(self)
        try:
            data_list.clear()
            open("NAFO-4TVN-Atlantic-Cod-otoliths.csv", "r")
            for i in range(101):
                line = csvfile.readline()
                elements = line.split(",")
                data = otolith.Otolith(elements[0][1:-1], elements[1][1:-1], elements[2][1:-1], elements[3][1:-1], elements[4], elements[5], elements[6][0:3])
                data_list.append(data)
            print("NAFO-4TVN-Atlantic-Cod-otoliths.csv file reloaded successfully!")
        except Exception:
            print("NAFO-4TVN-Atlantic-Cod-otoliths.csv file not found")

    # export the current data list into a new file
    def export(self):
        Controller.print_name(self)
        file_name = input("Enter file name: ")
        new_file = open(file_name + ".csv", "x")
        for data in data_list:
            new_file.write(data.__str__())
        new_file.close()
        print(file_name + ".csv created successfully!")

    # display the data as needed
    def display(self):
        Controller.print_name(self)
        print("There are {} records in the data list.".format(data_list.__len__() - 1))
        start = input("Number to start: ")
        end = input("Number to end: ")
        print("{:^13} {:^13} {:^13} {:^13} {:^7} {:^7} {:^17}".format("source", "latin_name", "english_name", "french_name", "year", "month", "number_otoliths"))
        for i in range(int(start), int(end) + 1):
            if i % 10 == 0:
                print("Program by Yunting Yin")
            print("{:^13} {:^13} {:^13} {:^13} {:^7} {:^7} {:^17}".format(data_list[i].get_source(), data_list[i].get_latin_name(), data_list[i].get_english_name(), data_list[i].get_french_name(), data_list[i].get_year(), data_list[i].get_month(), data_list[i].get_number()))

    # create a new data record into the data list
    def create(self):
        Controller.print_name(self)
        new_source = input("source: ")
        new_latin_name = input("latin_name: ")
        new_english_name = input("english_name: ")
        new_french_name = input("french_name: ")
        new_year = input("year: ")
        new_month = input("month: ")
        new_number_otoliths = input("number_otoliths: ")
        new_data = otolith.Otolith(new_source, new_latin_name, new_english_name, new_french_name, new_year, new_month, new_number_otoliths)
        data_list.append(new_data)
        print("The following data created successfully!")
        print(new_data.__str__())

    # edit a record in the data list
    def edit(self):
        Controller.print_name(self)
        print("There are {} records in the data list.".format(data_list.__len__() - 1))
        num = input("The number of data you want to edit: ")
        print("You are going to edit the following data:")
        edit_data = data_list[int(num)]
        print(edit_data.__str__())
        Controller.print_name(self)
        print("1. source")
        print("2. latin_name")
        print("3. english_name")
        print("4. french_name")
        print("5. year")
        print("6. month")
        print("7. number_otoliths")
        edit_num = input("Enter your option: ")
        if edit_num == "1":
            edit_string = input("source: ")
            edit_data.set_source(edit_string)
            print("New data: " + edit_data.__str__() + " updated successfully!")
        elif edit_num == "2":
            edit_string = input("latin_name: ")
            edit_data.set_latin_name(edit_string)
            print("New data: " + edit_data.__str__() + " updated successfully!")
        elif edit_num == "3":
            edit_string = input("english_name: ")
            edit_data.set_english_name(edit_string)
            print("New data: " + edit_data.__str__() + " updated successfully!")
        elif edit_num == "4":
            edit_string = input("french_name: ")
            edit_data.set_french_name(edit_string)
            print("New data: " + edit_data.__str__() + " updated successfully!")
        elif edit_num == "5":
            edit_string = input("year: ")
            edit_data.set_year(edit_string)
            print("New data: " + edit_data.__str__() + " updated successfully!")
        elif edit_num == "6":
            edit_string = input("month: ")
            edit_data.set_month(edit_string)
            print("New data: " + edit_data.__str__() + " updated successfully!")
        elif edit_num == "7":
            edit_string = input("number_otoliths: ")
            edit_data.set_number_otoliths(edit_string)
            print("New data: " + edit_data.__str__() + " updated successfully!")

    # delete a record in the data list
    def delete(self):
        Controller.print_name(self)
        print("There are {} records in the data list.".format(data_list.__len__() - 1))
        num = input("The number of data you want to delete: ")
        print("You are going to delete the following data:")
        delete_data = data_list[int(num)]
        print(delete_data.__str__())
        data_list.remove(delete_data)
        print("Data has been deleted. Now there are {} records in the data list.".format(data_list.__len__() - 1))

    # show a vertical bar chart depends on the range chosen by user
    def chart(self):
        print("There are {} records in the data list.".format(data_list.__len__() - 1))
        start = int(input("Number to start: "))
        end = int(input("Number to end: "))
        # a dictionary that saves the value of retrieved data
        group = {}
        x_axis = np.array([])
        y_axis = np.array([])
        for x in range(start, end + 1):
            source = data_list[x].get_source()
            number = int(data_list[x].get_number())
            # if the given key exists, add the value
            if source in group:
                group.update({source: group.get(source) + number})
            else:
                group.update({source: number})
        # configure the x and y axis of the vertical bar chart with the values in dictionary(group)
        for x, y in group.items():
            x_axis = np.append(x_axis, x)
            y_axis = np.append(y_axis, y)
        # show the chart
        pl.bar(x_axis, y_axis)
        pl.title("Atlantic Cod\nProgram by Yunting Yin")
        pl.xlabel("Source")
        pl.ylabel("Number of Otoliths")
        pl.show()

    # print my name
    def print_name(self):
        print("")
        print("Program by Yunting Yin")
        print("")

# Open NAFO-4TVN-Atlantic-Cod-otoliths.csv and return a stream and set it to csvfile
try:
    csvfile = open("C:/Desk/CP/Level 4/CST8333 Programming Language Research Project/git/CSV_CRUD/Part4/NAFO-4TVN-Atlantic-Cod-otoliths.csv", "r")
except Exception as e:
    print("NAFO-4TVN-Atlantic-Cod-otoliths.csv file not found")

# set an array
data_list = []

# reading 600 data from the dataset, the first line is column, so read 101 times
for i in range(601):
    line = csvfile.readline()
    elements = line.split(",")
    data = otolith.Otolith(elements[0][1:-1], elements[1][1:-1], elements[2][1:-1], elements[3][1:-1], elements[4], elements[5], elements[6][0:-1])
    data_list.append(data)
