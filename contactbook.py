import os

# Contact book to store contact information
contact_book = []

def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def add_contact():
    # Function to add a new contact
    print("Add Contact:")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contact_book.append(contact)
    print("Contact added successfully!")

def view_contact_list():
    # Function to display the list of all saved contacts
    print("\nContact List:")
    for index, contact in enumerate(contact_book, start=1):
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    # Function to search contacts by name or phone number
    search_term = input("\nEnter Name or Phone Number to search: ")
    results = []

    for contact in contact_book:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            results.append(contact)

    if results:
        print("\nSearch Results:")
        for result in results:
            print(f"Name: {result['name']}, Phone: {result['phone']}")
    else:
        print("No matching contacts found.")

def update_contact():
    # Function to update contact details
    view_contact_list()
    contact_index = int(input("\nEnter the index of the contact to update: ")) - 1

    if 0 <= contact_index < len(contact_book):
        contact = contact_book[contact_index]
        print("\nUpdate Contact:")
        contact['name'] = input(f"Enter new name ({contact['name']}): ") or contact['name']
        contact['phone'] = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
        contact['email'] = input(f"Enter new email ({contact['email']}): ") or contact['email']
        contact['address'] = input(f"Enter new address ({contact['address']}): ") or contact['address']

        print("Contact updated successfully!")
    else:
        print("Invalid index. Please try again.")

def delete_contact():
    # Function to delete a contact
    view_contact_list()
    contact_index = int(input("\nEnter the index of the contact to delete: ")) - 1

    if 0 <= contact_index < len(contact_book):
        deleted_contact = contact_book.pop(contact_index)
        print(f"Contact '{deleted_contact['name']}' deleted successfully!")
    else:
        print("Invalid index. Please try again.")

# Main program loop
while True:
    clear_screen()
    print("Contact Book\n")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    
    input("\nPress Enter to continue...")
