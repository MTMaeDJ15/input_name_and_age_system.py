list = []
coe_1_7 = {}

# Loop1: used to ask user for next input
while True:
    # Loop2: used to auto-retry when input raised an error
    while True:
        try:
            name = input("Pls input name: ")
            
            # Loop3: used to retry when number is not 11 characters
            while True:
                age = int(input("Pls input age: "))

                if len(str(age)) == 2:
                    # this is to stop Loop3
                    break
                else:
                    len(str(age)) >= 2
                    print("Please input 2 digit number!!")

            coe_1_7[0] = {
                "name" : name,
                "age" : age,
            }
           
            print(coe_1_7[0]["name"])
            print(coe_1_7[0]["age"])

            retry = input("Retry? ")
            # this is to stop Loop2
            break
        except:
            print("Ay mali!!!!")

    if retry != "yes":
        list.append(coe_1_7)

    elif retry == "no":
        break
    print(list)
