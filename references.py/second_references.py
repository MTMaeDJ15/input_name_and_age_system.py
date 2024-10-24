
def collect_data():
    people = []  # List to store people's information

    while True:
        # Collect name and age
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))

        # Append the data as a dictionary to the list
        people.append({"name": name, "age": age})

        # Ask if the user wants to input another data
        another = input("Do you want to input another person? (yes/no): ").lower()

        # Break the loop if the answer is no
        if another != "yes":
            break

    return people

# Function to find and print the oldest person
def find_oldest(people):
    # Find the oldest person using max() with key as age
    oldest_person = max(people, key=lambda person: person['age'])
    print("\nThe oldest person is:", oldest_person["name"], "with", oldest_person["age"], "years old.")

# Main function
def main():
    # Collect data from user
    people = collect_data()

    # Print the list of people
    print("\nList of people entered:")
    for person in people:
        print(f"Name: {person['name']}, Age: {person['age']}")

    # Find and print the oldest person
    find_oldest(people)

# Run the program
if __name__ == "__main__":
    main()

# This is from my programmer friend.