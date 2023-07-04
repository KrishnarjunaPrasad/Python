''' While Executing the code, Make sure to save this code in a Python file (e.g., contact_manager.py) and 
Create a CSV file named 'contacts.csv' in the same directory to store the contact data. 
You can run the code and interact with the contact management system through the console. '''

import csv

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, filename):
        self.filename = filename

    def add_contact(self, contact):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([contact.name, contact.phone, contact.email, contact.address])
        print('Contact added successfully.')

    def update_contact(self, search_key):
        contacts = self.read_contacts()
        found = False
        updated_contacts = []
        for contact in contacts:
            if search_key in [contact.name, contact.phone]:
                updated_name = input('Enter updated name: ')
                updated_phone = input('Enter updated phone: ')
                updated_email = input('Enter updated email: ')
                updated_address = input('Enter updated address: ')
                updated_contact = Contact(updated_name, updated_phone, updated_email, updated_address)
                updated_contacts.append(updated_contact)
                found = True
            else:
                updated_contacts.append(contact)
        if found:
            self.save_contacts(updated_contacts)
            print('Contact updated successfully.')
        else:
            print('Contact not found.')

    def delete_contact(self, search_key):
        contacts = self.read_contacts()
        found = False
        updated_contacts = []
        for contact in contacts:
            if search_key in [contact.name, contact.phone]:
                found = True
            else:
                updated_contacts.append(contact)
        if found:
            self.save_contacts(updated_contacts)
            print('Contact deleted successfully.')
        else:
            print('Contact not found.')

    def search_contact(self, search_key):
        contacts = self.read_contacts()
        found = False
        for contact in contacts:
            if search_key in [contact.name, contact.phone]:
                self.display_contact(contact)
                found = True
        if not found:
            print('Contact not found.')

    def read_contacts(self):
        contacts = []
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, phone, email, address = row
                contact = Contact(name, phone, email, address)
                contacts.append(contact)
        return contacts

    def save_contacts(self, contacts):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for contact in contacts:
                writer.writerow([contact.name, contact.phone, contact.email, contact.address])

    def display_contact(self, contact):
        print(f'Name: {contact.name}')
        print(f'Phone: {contact.phone}')
        print(f'Email: {contact.email}')
        print(f'Address: {contact.address}')
        print('---------------------------')

def main():
    contact_manager = ContactManager('contacts.csv')

    while True:
        print('Contact Management System')
        print('---------------------------')
        print('1. Add Contact')
        print('2. Update Contact')
        print('3. Delete Contact')
        print('4. Search Contact')
        print('0. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter name: ')
            phone = input('Enter phone: ')
            email = input('Enter email: ')
            address = input('Enter address: ')
            contact = Contact(name, phone, email, address)
            contact_manager.add_contact(contact)
        elif choice == '2':
            search_key = input('Enter name or phone of the contact to update: ')
            contact_manager.update_contact(search_key)
        elif choice == '3':
            search_key = input('Enter name or phone of the contact to delete: ')
            contact_manager.delete_contact(search_key)
        elif choice == '4':
            search_key = input('Enter name or phone of the contact to search: ')
            contact_manager.search_contact(search_key)
        elif choice == '0':
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
