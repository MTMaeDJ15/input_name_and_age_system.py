def collect_data():
    coe_1_7 = [] #This will be the list storage for the information inputted by the user.

    # Loop1: This is to ask the user to input information asked.
    while True:
            # Loop2: This is used to auto-retry when input raised an error.
        while True:
            name = input("Input your name: ")
                    
                    # Loop3: This is used to retry when number is not 2 digits. 
            while True:
                age = int(input("Input your age: "))

                if len(str(age)) <= 2: #This is to make sure that the user will input less than or equal 2 digits.
                        # This is to stop Loop 3. 
                    break
                else:
                    len(str(age)) >= 2
                    print("Ay mali!!!!") #Incase the user inputted greater than 2 digits required.

            coe_1_7.append({"name": name, "age": age})

            retry = input("Retry? (y/n): ").lower()

            if retry != "y":
                break #This is to stop Loop 2.
        
        return coe_1_7

def find_oldest(coe_1_7): # This define the oldest person and print it out.
    oldest_person = max(coe_1_7, key=lambda person: person['age'])
    print("\nThe oldest person is", oldest_person["name"], "who is", oldest_person["age"], "years old.")

def main(): #To define the whole program collect, print, and find the oldest person.
    coe_1_7 = collect_data()

    print("\nList of People entered:")
    for person in coe_1_7:
        print(f"Name: {person['name']}, Age: {person['age']}")
    
    find_oldest(coe_1_7)

if __name__ == "__main__":
    main()