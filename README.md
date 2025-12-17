# Phone Book CLI Application

A simple command-line phone book manager written in Python that allows users to store, search, and manage contacts with validated phone numbers.

## Features

- **Add Contacts**: Store names with validated phone numbers
- **Remove Contacts**: Delete contacts from the phone book
- **Search Contacts**: Look up phone numbers by name
- **List Contacts**: View all contacts in alphabetical order
- **Input Validation**: Ensures data integrity for names and phone numbers

## Installation

No installation required. Simply ensure you have Python 3.6+ installed.
```bash
python app.py
```
## Usage

### Main Menu

Upon running the application, you'll see the following menu:

Welcome to the phone book app!

Select an action:

1.  Add a contact
    
2.  Remove a contact
    
3.  Search for a contact
    
4.  View the phone book
    
5.  Exit

### Operations

#### 1. Add a Contact
- Enter a valid name (no digits allowed)
- Enter a phone number following validation rules
- Contact is saved to the phone book

#### 2. Remove a Contact
- Enter the name of the contact to delete
- Confirms removal or notifies if contact doesn't exist

#### 3. Search for a Contact
- Enter the name to search
- Displays the associated phone number if found

#### 4. View the Phone Book
- Lists all contacts alphabetically with their phone numbers

#### 5. Exit
- Closes the application

### Example Session

Welcome to the phone book app!

Select an action:

1.  Add a contact
    
2.  Remove a contact
    
3.  Search for a contact
    
4.  View the phone book
    
5.  Exit
    

Enter your choice (1-5): 1  
Enter the name of the contact: John Doe  
Enter the phone number of John Doe: +1234567890

Enter your choice (1-5): 4

Phone Book:

-   John Doe: +1234567890
    

Enter your choice (1-5): 5  
Goodbye!

## Validation Rules

### Name Validation
- Cannot contain digits
- Cannot be empty
- Whitespace is automatically trimmed

### Phone Number Validation
- Length: 6-11 characters
- Allowed characters: digits (0-9), plus sign (+), hyphen (-)
- Plus sign (+) must be at the start if present
- Maximum one plus sign
- Maximum one hyphen
- Examples of valid numbers:
  - `1234567`
  - `+1234567890`
  - `123-456-7890`
  - `+123456789`

### Invalid Examples
- `12-34-567` (multiple hyphens)
- `123++456` (multiple plus signs)
- `1+234567` (plus sign not at start)
- `12345` (too short)
- `123456789012` (too long)
- `123abc456` (contains letters)

## Code Structure

### Core Functions

- `valdiate_name(text)`: Validates contact names
- `valdiate_phone_number(name, num)`: Validates phone number format
- `add_contact()`: Adds a new contact with validation
- `remove_contact()`: Removes an existing contact
- `search_contact()`: Searches for a contact by name
- `list_contacts()`: Displays all contacts alphabetically
- `main()`: Main application loop and menu handler

### Data Storage

Contacts are stored in a dictionary (`contact = {}`), with names as keys and phone numbers as values. Data is lost when the program exits (no persistence).

## Requirements

- Python 3.6 or higher

## Potential Improvements

- **Data Persistence**: Save contacts to a file (JSON, CSV, or database)
- **Edit Functionality**: Update existing contact information
- **Multiple Numbers**: Support multiple phone numbers per contact
- **Email Support**: Add email addresses to contacts
- **Import/Export**: Load and save contact lists
- **Fuzzy Search**: Implement partial name matching
- **Phone Number Formatting**: Auto-format numbers for consistency
- **Duplicate Detection**: Warn when adding duplicate names
- **Contact Groups**: Organize contacts into categories

## Known Issues

- Contacts are not persisted between sessions
- Case-sensitive name matching (e.g., "John" vs "john" are different)
- Phone number validation is basic and may not match all international formats

## License

This project is licensed under the MIT License - see below for details:


## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the application.

