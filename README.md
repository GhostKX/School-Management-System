# School Management System

A Python-based command-line school management system to manage class assignments. This system allows you to add, delete, edit, and display class details, including class number, letter, and room number.

## Features

- **Class Management**:  
  - Add new classes and assign them to rooms.  
  - Delete existing class records by class number, letter, and room number.  
  - Edit class details (class number, letter, and room number).  
  - Display all current classes with their details.

- **Room Availability Check**:  
  - Prevent assigning a class to a room that is already occupied.

- **User-Friendly Interface**:  
  - Easy-to-follow, interactive menu for managing school classes.

## Requirements

- **Python 3.x** or higher.  
- No external libraries required.  

## How to Run

1. Clone or download this repository to your local machine.  
2. Open your terminal or command prompt.  
3. Navigate to the directory where the script is located.  
4. Run the script with the following command:  

```bash
python main.py
```

## Usage

The system provides the following options for class management:

- **Add**: Add a new class with a number, letter, and room number.
- **Delete**: Remove an existing class by entering the class number, letter, and room number.
- **Edit**: Modify the details of an existing class.
- **Show**: Display all current classes and their room assignments.
- **Exit**: Exit the program.

## Example Usage
```
**************************************************
Welcome to the School Management System!

Type in:
"Add" to add a new class.
"Delete" to delete a class.
"Edit" to edit class details.
"Show" to display all classes.
"Exit" to leave the system.
::: Add

Type in the class number: 101
Type in the class letter: A
Type in the class room number: 202

Class "101A" added to room number "202".
------------------------------------------------
Classes:
-------------------------------------
ID         Number     Letter    Room
-------------------------------------
1.         101        A         202
-------------------------------------
Total number of classes: 1.

------------------------------------------------
```

## Code Structure 

- **Class Data**: Class details (class number, letter, and room number) are stored in dictionaries, with separate dictionaries for each property (number, letter, room) and a combined dictionary ```class_all``` for easy management.
- **Room Management:**: The system ensures rooms are not double-booked by checking the availability of the room before assigning a class to it.

## Author

- Developed by **GhostKX**
- GitHub: **[GhostKX](https://github.com/GhostKX/School-Management-System)**

