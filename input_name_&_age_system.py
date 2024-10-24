import emoji 

def collect_data():
    data_entered = [] #This will be the list storage for the information inputted by the user.

    # Loop1: This is to ask the user to input information asked.
    while True:
            # Loop2: This is used to auto-retry when input raised an error.
        while True:
            text1 = emoji.emojize('Kindly enter the information asked below.:grinning_face_with_smiling_eyes:')
            print(text1)
            name = input("Input your name: ")
                    
                    # Loop3: This is used to retry when number is not 2 digits. 
            while True:
                age = int(input("Input your age: "))

                if len(str(age)) <= 2: #This is to make sure that the user will input less than or equal 2 digits.
                        # This is to stop Loop 3. 
                    break
                else:
                    len(str(age)) >= 2
                    print(" Please input a 2 digit number! ") #Incase the user inputted greater than 2 digits required.

            data_entered.append({"name": name, "age": age})

            retry = input("Do you want to input again?(yes/no): ").lower() 

            if retry != "yes":
                break #This is to stop Loop 2.
        
        return data_entered

def find_oldest(data_entered): # This define the oldest person and print it out.
    oldest_person = max(data_entered, key=lambda person: person['age'])
    print("\nThe oldest person is", oldest_person["name"], "who is", oldest_person["age"], "years old.")

def main(): #To define the whole program collect, print, and find the oldest person.
    data_entered = collect_data()

    print("\nList of People entered:")
    for person in data_entered:
        print(f"Name: {person['name']}, Age: {person['age']}")
    
    find_oldest(data_entered)

    text = emoji.emojize("It's Done. :blue_heart:")
    print(text)

if __name__ == "__main__":
    main()