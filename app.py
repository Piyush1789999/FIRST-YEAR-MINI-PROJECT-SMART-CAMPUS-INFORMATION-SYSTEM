import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
students = []
#STUDENT REGISTRATION AND GRADE EVALUATION(LAB1)

def register_stud():
    print("\n========== Student Registration ==========")
    student_id=input("Enter Student ID: ")
    name=input("Enter Student Name: ")
    age= input("Enter Age: ")
    score=float(input("Enter Exam Score (0-100): "))

    
    if score >= 90 and score <= 100:
        grade  = "A"
        remark = "Excellent"
    elif score >= 75:
        grade  = "B"
        remark = "Very Good"
    elif score >= 60:
        grade  = "C"
        remark = "Good"
    elif score >= 40:
        grade  = "D"
        remark = "Average"
    else:
        grade  = "F"
        remark = "Needs Improvement"
    student = {
        "id"     : student_id,
        "name"   : name,
        "age"    : age,
        "score"  : score,
        "grade"  : grade,
        "remark" : remark,
        "courses": []
    }
    students.append(student)

    print("\nStudent Registered Successfully!")
    print("Grade :", grade)
    print("Remark:", remark)

#COURSE ENROLLMENT MANAGEMENT SYSTEM(LAB2)
def enroll_courses():
    print("\n========== Course Enrollment ==========")

    id = input("Enter Student ID: ")

    student = None
    for i in students:
        if i["id"] == id:
            student = i
            break

    if student is None:
        print("Student not found!")
        return

    courses=[]
    max_courses=5

    print("=== Course Enrollment System ===")

    while True:
        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break
                course_name = input("Enter course name (or 'done' to finish): ")

        if course_name.lower() == "done":
            break

        credits = input("Enter credit value: ")

        if not credits.isdigit():
            print("Invalid credit value! Skipping entry...")
            continue

        credits = int(credits)

        if credits <= 0:
            print("Credit must be positive! Skipping entry...")
            continue

        courses.append((course_name, credits))
        print("Course '" + course_name + "' with " + str(credits) + " credits added.\n")

    student["courses"] = courses

    print("\n--- Enrollment Report ---")
    for course, credit in courses:
        print("Course:", course, ", Credits:", credit)
    print("Total courses enrolled:", len(courses))

#STUDENT RECORD STORAGE AND MANAGEMENT(LAB3)
def display_students():
    print("\n========== Student Records ==========")

    if len(students) == 0:
        print("No students registered yet.")
        return

    print("=== Student Records ===")
    for student in students:
        print("ID    :", student["id"])
        print("Name  :", student["name"])
        print("Age   :", student["age"])
        print("Score :", student["score"])
        print("Grade :", student["grade"])
        print("Remark:", student["remark"])
        print("-----------------------")

    print("\nALL STUDENTS STORED.")

#SEARCHING AND SORTING STUDENT ITS(LAB4)
def sort_student_ids():
    print("\n========== Sort Student IDs ==========")

    if len(students) == 0:
        print("No students registered yet.")
        return

    student_ids = [s["id"] for s in students]
    print("Original IDs:", student_ids)

    # Bubble Sort
    n = len(student_ids)
    bubble_ids = student_ids.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if bubble_ids[j] > bubble_ids[j + 1]:
                temp              = bubble_ids[j]
                bubble_ids[j]     = bubble_ids[j + 1]
                bubble_ids[j + 1] = temp
    print("Sorted IDs (Bubble Sort):", bubble_ids)

    # Selection Sort
    
   s_ids = student_ids.copy()
    for i in range(n):
        min_index = i
                for j in range(i + 1, n):
            if s_ids[j]<s_ids[min_index]:
                min_index = j
        temp=s_ids[i]
        s_ids[i]=s_ids[min_index]
        s_ids[min_index]=temp
    print("Sorted IDs (Selection Sort):",s_ids)


    target = input("\nEnter Student ID to search: ")

    # Linear Search
    found_index = -1
    for i in range(len(bubble_ids)):
        if bubble_ids[i] == target:
            found_index = i
            break
    if found_index != -1:
        print("Linear Search: ID", target, "found at index", found_index)
    else:
        print("Linear Search: ID not found")

    # Binary Search
    low         = 0
    high        = len(bubble_ids) - 1
    found_index = -1
    while low <= high:
        mid = (low + high) // 2
        if bubble_ids[mid] == target:
            found_index = mid
            break
        elif bubble_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if found_index != -1:
        print("Binary Search: ID", target, "found at index", found_index)
    else:
        print("Binary Search: ID not found")
#STUDENT FEE CALCULATIONS USING FUNCTIONS(LAB5)
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    total_fee = tuition_fee + hostel_fee + transportation_fee
    return total_fee

def fee_calculation():
    print("\n========== Fee Calculation ==========")

    tuition  = float(input("Enter Tuition Fee: "))
    hostel   = float(input("Enter Hostel Fee : "))
    transport = float(input("Enter Transportation Fee : "))

    total = calculate_fee(tuition, hostel, transport)

    print("\nTuition Fee    :", tuition)
    print("Hostel Fee     :", hostel)
    print("Transport Fee  :", transport)
    print("Total Fee      :", total)
#FILE BASED ACADEMIC RECORD MANAGEMENT(LAB6)
def saverecordsto_file():
    print("\n========== Save Records to File ==========")

    if len(students) == 0:
        print("No students to save.")
        return

    with open("student_records.txt", "w") as file:
        file.write("ID,Name,Marks\n")
        for s in students:
            file.write(s["id"] + "," + s["name"] + "," + str(s["score"]) + "\n")

    print("Student records written to file successfully.")
    print("\nReading stored records:")
    with open("student_records.txt", "r") as file:
        records = file.readlines()
        for record in records:
            print(record.strip())

    print("\nGenerating Report:")
    total_students = 0
    total_marks    = 0
    highest_marks  = -1
    top_student    = ""

    for record in records[1:]:
        parts  = record.strip().split(",")
        name   = parts[1]
        marks  = float(parts[2])
        total_students += 1
        total_marks    += marks
        if marks > highest_marks:
            highest_marks = marks
            top_student   = name

    average_marks = total_marks / total_students
    print("Total Students:", total_students)
    print("Average Marks :", average_marks)
    print("Top Student   :", top_student, "with", highest_marks, "marks")

def readrecords_from_file():
    print("\n========== Read Records from File ==========")
    try:
        with open("student_records.txt", "r") as file:
            records = file.readlines()
        print("Reading stored records:")
        for record in records:
            print(record.strip())
    
    except FileNotFoundError:
        print("File not found! Please save records first (Option 6).")

#DIRECTORY SCANNING WITH EXCEPTION HANDLING(LAB7)
class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing in the directory."""
    pass

def scan_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("Invalid directory path: " + path)

        print("\nScanning directory:", path)
        print()

        for root, dirs, files in os.walk(path):
            level      = root.replace(path, "").count(os.sep)
            indent     = " " * 4 * level
            print(indent + os.path.basename(root) + "/")
            sub_indent = " " * 4 * (level + 1)
            for f in files:
                print(sub_indent + f)
            if not files and not dirs:
                raise MissingFileOrFolderError("Empty folder detected: " + root)

    except FileNotFoundError as e:
        print("Error:", e)
    except MissingFileOrFolderError as e:
        print("Custom Error:", e)
    except Exception as e:
        print("Unexpected Error:", e)
#STUDENT PERFOMANCE ANALYSIS using NumPy, Pandas, and Matplotlib(LAB8)
def performance_analysis():
    print("\n========== Performance Analysis ==========")

    if len(students) < 2:
        print("Please register at least 2 students.")
        return

    names  = [s["name"]  for s in students]
    scores = [s["score"] for s in students]
    with open("student_performance.csv", "w") as f:
        f.write("Name,Score\n")
        for s in students:
            f.write(s["name"] + "," + str(s["score"]) + "\n")

    df = pd.read_csv("student_performance.csv")

    print("\n--- Raw Data ---")
    print(df.head())

    print("\n--- Statistical Summary ---")
    print(df.describe())

    scores_array = df["Score"].to_numpy()

    mean_score   = np.mean(scores_array)
    median_score = np.median(scores_array)
    std_score    = np.std(scores_array)

    print("\n--- NumPy Analysis ---")
    print("Mean Score  :", round(mean_score,   2))
    print("Median Score:", round(median_score, 2))
    print("Std Dev     :", round(std_score,    2))

    top_student = df.loc[df["Score"].idxmax(), "Name"]
        print("\n--- Top Performer ---")
    print("Top Student:", top_student)

    plt.bar(df["Name"], df["Score"], color=["blue", "green", "orange", "red", "purple"])
    plt.title("Average Scores per Student")
    plt.xlabel("Student Name")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.show()
#MAIN MENU
print("SMART CAMPUS SYSTEM")
while True:
    print("\n========= SMART CAMPUS SYSTEM =========")
    print("1.  Register Student")
    print("2.  Enroll Courses of students")
    print("3.  Display Students records ")
    print("4.  Sort and Searching Student IDs")
    print("5.  Search Student ID")
    print("6.   Student Fee Calculation")
    print("7.  Save Records to File")
    print("8.  Read Records from File")
    print("9.  Scan Directory")
    print("10. Performance Analysis of students")
    print("11. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register_stud()

    elif choice == "2":
        enroll_courses()

    elif choice == "3":
        display_students()

    elif choice == "4":
        sort_student_ids()

    elif choice == "5":
        name = input("Enter Student Name to search: ")
        found = False
        for s in students:
            if s["name"].lower() == name.lower():
                print("\nStudent Found!")
                print("ID    :", s["id"])
                print("Name  :", s["name"])
                print("Score :", s["score"])
                print("Grade :", s["grade"])
                found = True
        if not found:
            print("Student not found!")
    elif choice == "6":
        fee_calculation()

    elif choice == "7":
        saverecordsto_file()

    elif choice == "8":
        readrecords_from_file()

    elif choice == "9":
        path = input("Enter the directory path to scan: ")
        scan_directory(path)
    elif choice == "10":
        performance_analysis()

    elif choice == "11":
        print("\nExiting... Goodbye!")
        break

    else:
        print("Invalid choice! Enter a number between 1 and 11.")