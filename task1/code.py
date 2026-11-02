# University Scholarship Allocation System

students = []
eligible_students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    subjects = int(input("Enter number of subjects: "))
    subject_marks = []

    for j in range(subjects):
        mark = float(input("Enter subject mark: "))
        subject_marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    # Check eligibility
    if (aggregate >= 75 and
        all(mark >= 50 for mark in subject_marks) and
        attendance >= 75 and
        income <= 250000):

        eligible_students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

    else:
        print(name, "is Not Eligible")

# Sort students based on ranking rules
eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"]
    )
)

# Display results
print("\n===== SCHOLARSHIP ALLOCATION RESULTS =====")

if len(eligible_students) == 0:
    print("No students are eligible for scholarship.")

else:
    print("\nRank  Name       Aggregate  Attendance  Income")

    for rank, student in enumerate(eligible_students, start=1):
        print(
            rank,
            student["name"],
            student["aggregate"],
            student["attendance"],
            student["income"]
        )

print("\nProgram Completed")
