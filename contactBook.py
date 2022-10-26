# Create a contact Book using Python
names = []
phone_numbers = []

# Create a range of list as u wish
num = 3

# Let's take input of users
for i in range(num):
    name = input("Enter Name: ")
    phone_number = int(input("Phone Number: "))

    # Add these inputs to our list
    names.append(name)
    phone_numbers.append(phone_number)

# Print list of items
print("\nName\t\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

# Now if person wants a number of a person
search_term = input("\nEnter search term: ")

# Let's check if that search term is in our database or not
if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]

    # Let's print that result if available
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))

else:
    print("No results found")