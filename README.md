# Task Manager CLI 📋
### Video Demo: [Click Here](https://youtu.be/p_7_rblN5Jg?si=vRtDYWxuKvl-xzzu)
 ## **Authors: Nour Yacoub & Abi Ntumba**
 ## **GitHub username: @nouryacoub1**
 ## **Hult Section: BOS5**
 ## **DATE: 03/01/2025**

## 📌 Description

The Task manager CLI is a simple yet powerful command-line tool that lets you add, remove, and keep track of your tasks. What makes it unique and stand out from a basic note-taking app is that the program ensures that tasks are saved persistently in a tasks.json file, which prevents data loss even when the program is shut down. 
The main goal of this project was to develop a fully functional task manager using Python, with an emphasis on: 

- File handling (to store tasks permanently)
- User interaction (through a simple menu system)
- Function-based programming (to keep code modular and maintainable)
- Testing with pytest (to ensure the core function work correctly)
- The project demonstrates essential Python skills, such as file handling, using loops and conditionals, defining functions and implementing testing.

---

## 📌 Features

✅Add Tasks - Users can add new tasks to the list.
✅Remove Tasks - Users can delete tasks by specifiying the task name.
✅List Tasks - Displays all stored tasks in a numbered list.
✅Persistent storage - Saves tasks in a `tasks.json` file
✅Automated Testing- Uses `pytest` to verify functionality


---

## 📌 How to Install and Run
1️⃣ Clone the Repository

git clone https://github.com/YOUR_GITHUB_USERNAME/task-manager.git
cd task-manager

2️⃣ Install Dependencies
Install pytest (used for testing):
sh
CopyEdit
pip install -r requirements.txt

3️⃣ Run the Application
To start the Task Manager CLI:
sh
CopyEdit
python project.py

This will display the menu where you can choose an option.

--- 

## 📌 How It Works
🔹 1. Adding a Task
Example:
vbnet
CopyEdit
Choose an option: 1
Enter the task: Complete the Python project
Task 'Complete the Python project' added!

The task is saved in tasks.json so that it persists even after the program is closed.
🔹 2. Listing Tasks
Example:
yaml
CopyEdit
Choose an option: 3
Your Tasks:
1. Complete the Python project

🔹 3. Removing a Task
Example:
vbnet
CopyEdit
Choose an option: 2
Enter the task to remove: Complete the Python project
Task 'Complete the Python project' removed!

🔹 4. Exiting the Program
Example:
vbnet
CopyEdit
Choose an option: 4
Goodbye!

The program will close, but tasks remain stored in tasks.json.

---

## 📌 Code Explanation
📂 Project Structure
bash
CopyEdit
/project
│── project.py         # Main Python script
│── test_project.py    # Test cases using pytest
│── requirements.txt   # Dependencies
│── README.md          # Documentation
│── tasks.json         # Stores tasks (auto-generated)

🔹 project.py (Main Script)
Contains the core functions: add_task(), remove_task(), and list_tasks().
Implements file handling (tasks.json) to store tasks persistently.
Includes a menu-driven CLI that allows user interaction.
🔹 test_project.py (Unit Testing)
Uses pytest to test key functions.
Ensures:
add_task() correctly adds tasks.
remove_task() removes tasks properly.
list_tasks() correctly displays tasks.
🔹 tasks.json (Storage)
Stores tasks persistently.
Automatically created when running project.py.

---

## 📌 Design Decisions
Why Store Tasks in JSON Instead of a Database?
- JSON is lightweight, easy to read, and requires no setup.
- Perfect for small-scale applications like this.
Why Use pytest for Testing?
- pytest allows for automated testing.
- Ensures that code does not break when modified.
Challenges Faced
- Handling JSON errors when the file is empty or corrupted.
- Ensuring that user inputs are validated to prevent crashes.

---

## 📌 Running Automated Tests
To ensure all functions work correctly, run:
sh
CopyEdit
pytest

---

## 📌 Expected Output:
diff
CopyEdit
============================= test session starts =============================
collected 3 items
test_project.py ...                                                      [100%]

============================== 3 passed in 0.12s ==============================

If you see 3 passed, your tests have passed successfully! ✅

---

## 📌 Future Enhancements 
- Add due dates for tasks
- Creat a GUI using Tkinter
- Store tasks in an SQlite data base

## 📌 Conclusion
The Task Manager CLI is a practical and fictional Python project that highlights key programming skills such as managing files, handling user input and implementing testing. 

By adding future enhancements like a graphical interface and database storage, this project could be expanded into a full-featured task management system.
