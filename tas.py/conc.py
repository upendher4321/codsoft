def display_contacts(contact_book):
    """Display all contacts in the contact book."""
    if contact_book:
        print("\nContacts List:")
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")
    else:
        print("\nNo contacts found!")
def add_contact(contact_book):
    """Add a new contact to the contact book."""
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contact_book[name] = phone
    print(f"Contact for {name} added.")
def update_contact(contact_book):
    """Update an existing contact in the contact book."""
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        phone = input(f"Enter new phone number for {name}: ")
        contact_book[name] = phone
        print(f"Contact for {name} updated.")
    else:
        print("Contact not found!")
def delete_contact(contact_book):
    """Delete a contact from the contact book."""
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact for {name} deleted.")
    else:
        print("Contact not found!")
def main():
    """Main function to run the contact book."""
    contact_book = {}
    while True:
        print("\nContact Book Menu:")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit") 
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == "1":
            display_contacts(contact_book)
        elif choice == "2":
            add_contact(contact_book)
        elif choice == "3":
            update_contact(contact_book)
        elif choice == "4":
            delete_contact(contact_book)
        elif choice == "5":
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()