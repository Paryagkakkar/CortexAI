students=[]
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. remove student")
    print("4. sort students")
    print("5. exit")
    choice=input("enter your choice: ")
    if choice=="1":
        name=input("enter student name: ")
        students.append(name)
        print("student added successfully")
    elif choice=="2":
        if len(students)==0:
            print("no students found")
        else:
            for student in students:
                print(student)
    elif choice=="3":
        if len(students)==0:
            print("no students found")
        else:
            removed_student=students.pop()
            print(f"removed student: {removed_student}")

    elif choice=="4":
        if len(students)==0:
            print("no students found")
        else:
            students.sort()
            print("students sorted successfully",students)
    elif choice=="5":
        print("thank you for using student management system")
        break
    else:
        print("invalid choice")
