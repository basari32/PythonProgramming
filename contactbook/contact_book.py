import json

contacts = []

def main():
    load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")



def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    print(f"Contact '{name}' added!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")

def search_contact():
    query = input("Enter name to search: ").lower()
    results = [c for c in contacts if query in c["name"].lower()]
    if results:
        for c in results:
            print(f"{c['name']} | {c['phone']} | {c['email']}")
    else:
        print("No matching contacts found.")

def delete_contact():
    name = input("Enter name to delete: ").lower()
    global contacts
    contacts = [c for c in contacts if c["name"].lower() != name]
    save_contacts()
    print("Contact deleted (if it existed).")


def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []

main()