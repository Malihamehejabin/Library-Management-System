# 📖 Library Management System

A lightweight Python application that simulates a basic library.
Built with Object-Oriented Programming (OOP) principles, this project makes it easy to add books, borrow them, and return them — all while preventing duplicate borrowing.

## ✨ Key Features

✅ Add Books – Store books with title and author.

✅ Borrow Books – Borrow available books.

✅ Return Books – Return borrowed books.

✅ Smart Validation – Prevents double borrowing or returning non-existent books.

✅ Easy-to-Extend – Designed with OOP for future scalability.

## 🛠️ Tech Stack

Language: Python 3.x

Concepts: Classes, Objects, Encapsulation, State Management

## ⚡ Quick Start
1️⃣ Clone Repository
```
git clone https://github.com/your-username/library-management.git
cd library-management
```
2️⃣ Run Program
```
python library_management.py
```

🧑‍💻 Example Usage
```python
# Create a library instance
library = Library()

# Add books
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

# Borrow a book
library.borrow_book("1984")  
# Output: You have borrowed '1984'

# Return a book
library.return_book("1984")  
# Output: You have returned '1984'
```

📊 Sample Output
```
You have borrowed '1984'
You have returned '1984'
```

📂 Project Structure
```
library-management/
│── library_management.py   # Main program logic
│── README.md               # Documentation
```

## 🚀 Future Improvements

🔹 Track multiple copies of a book.

🔹 Support search by author/title.

🔹 Add a user system (track who borrowed what).

🔹 Save/load data to JSON/CSV.

🔹 Create a GUI (Tkinter/PyQt) or Web App (Flask/Django).

## 👨‍💻 Author

Crafted with ❤️ by Maliha Mehejabin

**⚡ Pro Tip: You can use this system as a foundation for a full-fledged digital library app with persistence and user management.**
