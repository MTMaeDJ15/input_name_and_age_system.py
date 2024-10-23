coe_1_7 = {}

# Loop1: used to ask user for next input
while True:
    # Loop2: used to auto-retry when input raised an error
    while True:
        try:
            name = input("Pls input name: ")
            age = int(input("Pls input age: "))
            add = input("Pls input add: ")
            
            # Loop3: used to retry when number is not 11 characters
            while True:
                number = input("Pls input number: ")

                if len(number) == 11:
                    # this is to stop Loop3
                    break

            coe_1_7[name] = {
                "age" : age,
                "add" : add,
                "number": number
            }
           
            print(coe_1_7[name]["age"])
            print(coe_1_7[name]["add"])
            print(coe_1_7[name]["number"])

            retry = input("Retry? ")
            # this is to stop Loop2
            break
        except:
            print("Ay mali!!!!")

    if retry == "n":
        # this is to stop Loop1
        break
    elif retry != "y":
        print("Invalid")