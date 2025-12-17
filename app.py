contact = {}


def valdiate_name(text):
    if any(char.isdigit() for char in text):
        print(f"{text} is not a valid phone number.", end=" ")
        print("It contains digit\n")
        return False
    if not text:
        print("Name cannot be empty\n")
        return False
    return True


def valdiate_phone_number(name, num):
    if num.count("+") > 1 or ("+" in num and not num.startswith("+")):
        print(f"{num} is not a valid phone number.", end="")
        print("It should contain a plus sign (+) at the start.\n")
        return False
    if num.count("-") > 1:
        print(
            f"{num} is not a valid phone number. It should contain only digits, one optional hyphen."
        )
        return False
    allowed = set("0123456789+-")
    if not all(char in allowed for char in num):
        print(f"{num} is not a valid phone number. Invalid characters present.\n")
        return False
    if not (6 <= len(num) <= 11):
        print(
            f"{num} is not a valid phone number. It should contain only digits, one optional hyphen."
        )
        return False
    return True


def add_contact():
    text = input("Enter the name of the contact: ").strip()
    if not valdiate_name(text):
        return
    num = input(f"Enter the phone number of {text}: ").strip()
    if not valdiate_phone_number(text, num):
        return
    contact[text] = num


def remove_contact():
    name = input("Enter the name of the contact to remove: ").strip()
    if not valdiate_name(name):
        return
    if name in contact:
        del contact[name]
        print(f"Contact {name} has been removed\n")
    else:
        print(f"\nNo contact found with name: {name}\n")


def search_contact():
    text = input("Enter the name of the contact to search for: ")
    if not valdiate_name(text):
        return
    if text in contact:
        print(f"{text}'s phone number is:", contact.get(text, 0), "\n")
    else:
        print(f"{text}'s not in the contact\n")


def list_contacts():
    print("\nPhone Book:")
    for key, title in sorted(contact.items()):
        print(f"- {key}: {title}")
    print()


def main():
    while True:
        print("Welcome to the phone book app!\n")
        print("Select an action:")
        print("1. Add a contact")
        print("2. Remove a contact")
        print("3. Search for a contact")
        print("4. View the phone book")
        print("5. Exit\n")
        choice_raw = input("Enter your choice (1-5): ").strip()
        if not choice_raw.isdigit():
            print("Please enter a number.\n")
            continue
        num = int(choice_raw)
        if num < 1 or num > 5:
            print(
                f"{num} is not a valid choice. Please select a number between 1 and 5.\n"
            )
            continue
        if num == 1:
            add_contact()
        elif num == 2:
            remove_contact()
        elif num == 3:
            search_contact()
        elif num == 4:
            list_contacts()
        elif num == 5:
            print("Goodbye!\n")
            break


if __name__ == "__main__":
    main()
