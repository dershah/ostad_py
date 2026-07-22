# Assignment: Library Management
# System (Python OOP)
# Title
# Library Management System using Python OOP
# Objective
# Develop a console-based Library Management System using Object-Oriented Programming
# (OOP) concepts in Python. The project should demonstrate your understanding of classes,
# objects, constructors, inheritance, encapsulation, properties, class methods, static methods,
# and composition.
# Learning Outcomes
# After completing this assignment, students should be able to:
# ● Create and use classes and objects
# ● Work with constructors (__init__)
# ● Use instance variables and methods
# ● Use class variables and class methods
# ● Create static methods
# ● Apply encapsulation using private attributes
# ● Use @property for getter and setter
# ● Implement inheritance and method overriding
# ● Apply composition between classes
# ● Organize Python projects into multiple files
# ● Push a complete project to GitHub
# Project Description
# A library wants to replace its paper-based system with a simple software application.
# The system should allow a librarian to:
# ● Add new books
# ● Register members
# ● Borrow books
# ● Return books
# ● View all books
# ● View all members
# ● Search books by title
# ● Exit the program
# All data will remain in memory (database is not required).
# Required Classes
# 1. Person (Parent Class)
# Attributes
# name
# age
# Methods
# display_info()
# 2. Member (Child of Person)
# Additional Attributes
# member_id
# borrowed_books
# Methods
# borrow_book()
# return_book()
# display_info() (Override)
# 3. Book
# Attributes
# title
# author
# isbn
# available
# Methods
# display_book()
# Use encapsulation for available.
# Create
# Getter
# Setter
# Read-only property if needed
# 4. Library
# Attributes
# books
# members
# Methods
# add_book()
# register_member()
# borrow_book()
# return_book()
# show_books()
# show_members()
# search_book()
# Use composition, because a Library contains Books and Members.
# Sample Input / Output
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# 1. Add Book
# 2. Register Member
# 3. Borrow Book
# 4. Return Book
# 5. Show All Books
# 6. Show All Members
# 7. Search Book
# 8. Exit
# Enter your choice: 1
# ----- Add New Book -----
# Enter Book Title : Python Programming
# Enter Author : John Smith
# Enter ISBN : B101
# Book added successfully!
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# 1. Add Book
# 2. Register Member
# 3. Borrow Book
# 4. Return Book
# 5. Show All Books
# 6. Show All Members
# 7. Search Book
# 8. Exit
# Enter your choice: 1
# ----- Add New Book -----
# Enter Book Title : Data Structures
# Enter Author : Ahmed Ali
# Enter ISBN : B102
# Book added successfully!
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 2
# ----- Register Member -----
# Enter Member ID : M001
# Enter Name : Naimur
# Enter Age : 23
# Member registered successfully!
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 2
# ----- Register Member -----
# Enter Member ID : M002
# Enter Name : Sara
# Enter Age : 21
# Member registered successfully!
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 5
# ------------- BOOK LIST -------------
# ISBN : B101
# Title : Python Programming
# Author : John Smith
# Status : Available
# -------------------------------------
# ISBN : B102
# Title : Data Structures
# Author : Ahmed Ali
# Status : Available
# -------------------------------------
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 6
# ----------- MEMBER LIST ------------
# Member ID : M001
# Name : Naimur
# Age : 22
# Borrowed Books : 0
# ------------------------------------
# Member ID : M002
# Name : Sara
# Age : 21
# Borrowed Books : 0
# ------------------------------------
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 3
# ------ Borrow Book ------
# Enter Member ID : M001
# Enter Book ISBN : B101
# Book borrowed successfully.
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 5
# ------------- BOOK LIST -------------
# ISBN : B101
# Title : Python Programming
# Author : John Smith
# Status : Borrowed
# -------------------------------------
# ISBN : B102
# Title : Data Structures
# Author : Ahmed Ali
# Status : Available
# -------------------------------------
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 3
# ------ Borrow Book ------
# Enter Member ID : M002
# Enter Book ISBN : B101
# Sorry! This book is currently unavailable.
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 7
# ------ Search Book ------
# Enter Book Title : Python Programming
# Book Found!
# ISBN : B101
# Title : Python Programming
# Author : John Smith
# Status : Borrowed
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 4
# ------ Return Book ------
# Enter Member ID : M001
# Enter Book ISBN : B101
# Book returned successfully.
# Press Enter to continue...
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 5
# ------------- BOOK LIST -------------
# ISBN : B101
# Title : Python Programming
# Author : John Smith
# Status : Available
# -------------------------------------
# ISBN : B102
# Title : Data Structures
# Author : Ahmed Ali
# Status : Available
# -------------------------------------
# Press Enter to continue...
# Example Error Cases
# Duplicate ISBN
# Enter your choice: 1
# Enter Book Title : Python Programming
# Enter Author : John Smith
# Enter ISBN : B101
# Error: ISBN already exists.
# Duplicate Member ID
# Enter your choice: 2
# Enter Member ID : M001
# Enter Name : Hasan
# Enter Age : 20
# Error: Member ID already exists.
# Invalid Member
# Enter your choice: 3
# Enter Member ID : M999
# Enter Book ISBN : B101
# Member not found.
# Book Not Found
# Enter your choice: 3
# Enter Member ID : M001
# Enter Book ISBN : B999
# Book not found.
# Search Not Found
# Enter your choice: 7
# Enter Book Title : Java
# Book not found.
# Invalid Age
# Enter your choice: 2
# Enter Member ID : M003
# Enter Name : Rahim
# Enter Age : -5
# Error: Age must be greater than 0.
# Exit
# =========================================
# LIBRARY MANAGEMENT SYSTEM
# =========================================
# Enter your choice: 8
# Thank you for using Library Management System.
# Goodbye!
# Validation Rules
# ● Book ISBN must be unique.
# ● Member ID must be unique.
# ● Age must be greater than 0.
# ● Book title cannot be empty.
# ● Author name cannot be empty.
# ● Prevent borrowing an already borrowed book.
# ● A member cannot borrow the same book twice.
# Exception Handling
# Handle the following errors using try-except:
# ● Invalid menu choice
# ● Invalid age input
# ● Empty input
# ● Duplicate ISBN
# ● Duplicate Member ID
# ● Unexpected runtime errors
# The program should not crash because of invalid input.
# GitHub Submission Rules
# 1. Create a public GitHub repository named:
# python-library-management-system
# 2. Push the complete project to GitHub.
# 3. Submit your public github repository link
# Submission: Submit the GitHub repository link before the deadline