import os, json


# opens and reads the json file
def read_cars(my_data_file):
    try:
        with open(my_data_file, 'r') as file:
            json_string = file.read()
            return json.loads(json_string)
    except:
        return []


# prints the cars list
def print_func(cars):
    os.system('cls')
    for car in cars:
        print(f"ID: {car['ID']}, Color: {car['Color']}, Model: {car['Model']}, Brand: {car['Brand']}")
        print("-----------------------------------")


# adds new cars to the list with ID
def add_func(cars):
    os.system('cls')
    # goes through 3 inputs for color/model/brand
    color = input("Enter color: ")
    model = input("Enter model: ")
    brand = input("Enter brand: ")
    # ensures that IDs are not duplicated, adds +1 to the max ID
    new_id = max([car["ID"] for car in cars], default=0) + 1 
    # adds the new car to the list
    cars.append({"ID": new_id, "Color": color, "Model": model, "Brand": brand})
    print(f"Added car with ID {new_id}")


# exits the program with an option to save
def exit_func(cars, my_data_file):
    os.system('cls')
    inputCar = input("Do you want to save? (y/n)")
    if inputCar == "y":
        #write list to file
        json_string = json.dumps(cars)
        # save the list in a file
        with open(my_data_file, 'w') as file:
            file.write(json_string)
        print("Saving and Exiting..")
        exit()
    elif inputCar == "n":
        print("Exiting..")
        exit()
    else:
        print("invalid input")



# deletes a car from the cars list by ID
def del_func(cars):
    os.system('cls')
    print_func(cars)
    input_id = input("Enter ID to delete or -1 to cancel: ")

    ids = [car["ID"] for car in cars]
    # checks if the input ID is in the list of IDs
    if int(input_id) in ids:
        # uses input ID to delete the entry
        cars[:] = [car for car in cars if car["ID"] != int(input_id)]
        print(f"Deleted car with ID {input_id}")
    else:
        print(f"Unable to delete car with ID {input_id}: Not in the list.")



# searches for a car in the cars list by ID
def search_func(cars):
    os.system('cls')
    input_id = input("Enter ID to search: ")
    # gets all the IDs
    ids = [car["ID"] for car in cars] 
    print("Total IDs: ",ids) # debug
    # checks if the input ID is in the list of IDs
    if int(input_id) in ids:
        # find the car with the specific ID
        found_car = next(car for car in cars if car["ID"] == int(input_id))

        # prints the rest of the entry without the ID
        print(f"Car with ID {input_id} found:")
        for key, value in found_car.items():
            if key != "ID":
                print(f"{key}: {value}")
    else:
        print(f"Car with ID {input_id} is not in the list.")




