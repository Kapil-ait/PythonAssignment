# Blood Bank Management System

donors = []

# Function to add donor
def add_donor():
    name = input("Enter Donor Name: ")
    blood_group = input("Enter Blood Group: ")
    phone = input("Enter Phone Number: ")
    city = input("Enter City: ")

    donor = {
        "name": name,
        "blood_group": blood_group,
        "phone": phone,
        "city": city
    }

    donors.append(donor)
    print("Donor added successfully!\n")


# Function to search donor
def search_donor():
    bg = input("Enter Blood Group to Search: ")
    found = False

    for donor in donors:
        if donor["blood_group"].lower() == bg.lower():
            print("\nDonor Found")
            print("Name:", donor["name"])
            print("Blood Group:", donor["blood_group"])
            print("Phone:", donor["phone"])
            print("City:", donor["city"])
            print("---------------------")
            found = True

    if not found:
        print("No donor found with this blood group.\n")


# Function to show all donors
def show_donors():
    if len(donors) == 0:
        print("No donors available.\n")
        return

    print("\nList of All Donors")
    for donor in donors:
        print("Name:", donor["name"])
        print("Blood Group:", donor["blood_group"])
        print("Phone:", donor["phone"])
        print("City:", donor["city"])
        print("---------------------")


# Main program
while True:
    print("\n===== Blood Bank Management System =====")
    print("1. Add Donor")
    print("2. Search Donor by Blood Group")
    print("3. Show All Donors")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_donor()

    elif choice == "2":
        search_donor()

    elif choice == "3":
        show_donors()

    elif choice == "4":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")