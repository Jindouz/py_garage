import os
from helper import *
from enum import Enum


class Actions(Enum):
    PRINT = 1
    ADD = 2
    DELETE = 3
    SEARCH = 4
    EXIT = 5


cars = []
my_data_file = "list.json"


def menu():
  print("==Garage Menu==")
  for x in Actions:
    print(f'{x.name} - {x.value}')
  return input("Enter your selection: ")


def main():
    os.system('cls')
    global cars
    # calls the function to read the cars list from file (in helper.py)
    cars = read_cars(my_data_file)

    while (True):
        userSelection = menu()
        # menu logic with calls to functions from helper.py
        if Actions(int(userSelection)) == Actions.EXIT: exit_func(cars, my_data_file)
        elif Actions(int(userSelection)) == Actions.PRINT: print_func(cars)
        elif Actions(int(userSelection)) == Actions.ADD: add_func(cars)
        elif Actions(int(userSelection)) == Actions.DELETE: del_func(cars)
        elif Actions(int(userSelection)) == Actions.SEARCH: search_func(cars)


if __name__ == '__main__':
    main()
