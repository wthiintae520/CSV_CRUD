"""
Created on October 13, 2022,
Modified on October 14, 2022,
Description: This file control the interaction with user
@author: Yunting Yin
"""
import controller
c = controller.Controller()

#in charge of the interaction with user
class View:
    
    #start the program and run the program until user want to exit it
    def start_app(self):
        while True:
            choice = view.display_menu()
            view.execute_menu(choice)
            if choice == "7": 
                break
    
    #display the menu and return the user input
    def display_menu(self):
        print("Program by Yunting Yin")
        print("")
        print("1. Reload")
        print("2. Export")
        print("3. Display")
        print("4. Create")
        print("5. Edit")
        print("6. Delete")
        print("7. Exit")
        choice = input("Enter your option: ")
        return choice

    #execute the menu by user's choice
    def execute_menu(self, choice):
        if choice == "1":
            c.reload()
        elif choice == "2":
            c.export()
        elif choice == "3":
            c.display()
        elif choice == "4":
            c.create()
        elif choice == "5":
            c.edit()
        elif choice == "6":
            c.delete()
        elif choice == "7":
            print("Good bye!")
        else:
            print("Wrong input, try again")
            print("")
            print("")
            
#create the View object
view = View()

#start the program
view.start_app()
