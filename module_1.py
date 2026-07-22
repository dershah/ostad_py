import math
# Build a simple Python console application using the topics you have learned this week.
# Project Requirements
# Create a Python program that performs the following tasks:

# 1. Student Information
# â— Ask the user to enter:
# â—‹ Student Name
# â—‹ Student ID
# â—‹ Department
# Store the information using appropriate variables.
print("# 1. Student Information")

student={
    "id": 2355489,
    "name": "Max Mustermann",
    "department": "Computer Science"
}

print(f"Student: {student}")

for key, value in student.items():
    print(key," - ", value)

print()

# 2. Subject Marks
# Create a list of the following subjects:
# ["Python", "Math", "English", "Physics", "ICT"]
# Using a for loop, ask the user to enter marks for each subject.
# Store all marks in a dictionary like:
# {
# "Python": 90,
# "Math": 85,
# ...
# }
print("# 2. Subject Marks")

marks={}
subjects= ["Python", "Math", "English", "Physics", "ICT"]
for subject in subjects:
    marks[subject] = int(input(f"Enter the marks for {subject}: "))

print (marks)

print(marks.keys())
print(marks.values())

print()

# 3. Calculate Result
# Calculate
# â— Total Marks
# â— Average Marks
# â— Highest Mark
# â— Lowest Mark
# Use Python's built-in math functions where possible.


print("# 3. Calculate Result")

marks_values=marks.values()
total= sum(marks_values)
length= len(marks_values)
average= total/length
round_mark= round(average)
highest_mark=max(marks_values)
lowest_mark=min(marks_values)


print(f"Total Marks: {total}")
print(f"Average Marks: {average}")

print(f"Round Marks: {round_mark}")
print(f"Celi Marks: {math.ceil(average)}") # rounds a number up to the nearest integer.
print(f"floor Marks: {math.floor(average)}") # rounds a number down to the nearest integer

print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print()


print()
# 4. Grade Calculation
# Using if-elif-else, assign grades.
# Average Grade
# 80-100 A+
# 70-79 A
# 60-69 A
# 50-59 B
# 40-49 C
# Below 40 F

print("# 4. Grade Calculation")

grade= "F"
if(round_mark>=80):
    grade= "A+"
elif(round_mark>=70 and round_mark<80):
    grade= "A"
elif(round_mark>=60 and round_mark<70):
    grade= "A-"
elif(round_mark>=50 and round_mark<60):
    grade= "B"
elif(round_mark>=40 and round_mark<50):
    grade= "C"

print(grade)

print()

# 5. Pass or Fail
# If any subject mark is below 40, display
# Status: Failed
# Otherwise
# Status: Passed

print("# 5. Pass or Fail")

result= "Passed âœ…"
for key, value in marks.items():
    if(value<40):
        result= "Failed ðŸ’¥"
        break
print(result)
print()

# 6. Password Verification
# Ask the user to enter a password.
# Correct password:
# python123
# Use a while loop until the correct password is entered.

print("# 6. Password Verification")

correct_password=False
failed_attempt= 0

while not correct_password:
    get_password= input("Enter your Password: ")
    if (get_password == 'python123'):
        print("Password is a match âœ…. Authorization Granted")
        correct_password=True
        break
    else:
        print("Password doesn't match âŒ. Please try again")
        failed_attempt+=1
        print(f"Failed Attempts: {failed_attempt} â€¼ï¸")

print()

# 7. String Operations
# Display:
# â— Student name in uppercase
# â— Student name in lowercase
# â— Length of the student name
# â— First three characters
# â— Last three characters

print("# 7. String Operations")

print(student["name"].upper())
print(student["name"].lower())

print(len(student["name"]))
print(student["name"][:3])
print(student["name"][-3:])
print()

# 8. Set Example
# Create two sets.
# sports = {"Football", "Cricket", "Badminton"}
# clubs = {"Programming", "Cricket", "Photography"}
# Display
# â— Common items
# â— All unique items

print("# 8. Set Example")

sports = {"Football", "Cricket", "Badminton"}
clubs = {"Programming", "Cricket", "Photography"}

common_set=sports & clubs
print(f"â— Common items: {common_set}")

unique_set=sports ^ clubs
print(f"â— Unique items: {unique_set}")

print()
# 9. Tuple Example
# Create a tuple containing weekdays.
# Display
# â— First day
# â— Last day
# â— Total number of days

print("# 9. Tuple Example")

days= ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(f"â— First day: {days[0]}")
print(f"â— Last day: {days[len(days)-1]}")
print(f"â— Total number of days: {len(days)}")

print()

# 10. Final Report
# Display the report like this:
# ==============================
# STUDENT REPORT
# ==============================
# Name : Rahim
# ID : 221-15-001
# Department: CSE
# Python : 90
# Math : 85
# English : 80
# Physics : 95
# ICT : 88
# ------------------------------
# Total : 438
# Average : 87.6
# Highest : 95
# Lowest : 80
# Grade : A+
# Status : Passed


print("# 10. Final Report")
print("# ==============================")
print("# # STUDENT REPORT")
print("# ==============================")
print(f"# Name : {student["name"]}")
print(f"# ID : {student["id"]}")
print(f"# Department: {student["department"]}")
print(f"# Python : {marks["Python"]}")
print(f"# Math : {marks["Math"]}")
print(f"# English : {marks["English"]}")
print(f"# Physics : {marks["Physics"]}")
print(f"# ICT : {marks["ICT"]}")
print("# ------------------------------")
print(f"# Total : {total}")
print(f"# Average : {round_mark}")
print(f"# Highest : {highest_mark}")
print(f"# Lowest : {lowest_mark}")
print(f"# Grade : {grade}")
print(f"# Status : {result}")
print()
