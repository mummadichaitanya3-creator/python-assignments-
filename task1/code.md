## 1. Problem Statement

University Scholarship Allocation: Design a system that evaluates applicants using aggregate marks, subject-wise minimum scores, attendance, and income criteria, ranks eligible students, and resolves ties using predefined rules. 

## 2. Algorithm

1. Start the program.
2. Enter the number of students.
3. Enter each student's name, aggregate marks, subject marks, attendance, and family income.
4. Check the eligibility conditions:
   - Aggregate marks ≥ 75%.
   - All subject marks ≥ 50%.
   - Attendance ≥ 75%.
   - Family income ≤ ₹2,50,000.
5. If all conditions are satisfied, add the student to the eligible list.
6. Sort eligible students using:
   - Highest aggregate marks.
   - Highest attendance.
   - Lowest family income.
7. Display the eligible students with their ranks.
8. If no students are eligible, display a message.
9. Stop.

## 3. Flowchart

``` mermaid
flowchart TD
    A([Start]) --> B[/Enter number of students/]
    B --> C[/Enter student details/]
    C --> D{Check eligibility}
    D -->|Eligible| E[Add to eligible list]
    D -->|Not Eligible| F[Skip student]
    E --> G{More students?}
    F --> G
    G -->|Yes| C
    G -->|No| H[Sort eligible students]
    H --> I[Assign ranks]
    I --> J[/Display scholarship list/]
    J --> K([Stop])
```

## 4. Sample Input

```
Enter number of students: 3

Enter details of Student 1
Enter student name: Ravi
Enter aggregate marks: 85
Enter number of subjects: 3
Enter subject mark: 80
Enter subject mark: 90
Enter subject mark: 85
Enter attendance percentage: 90
Enter annual family income: 200000

Enter details of Student 2
Enter student name: Kumar
Enter aggregate marks: 80
Enter number of subjects: 3
Enter subject mark: 75
Enter subject mark: 80
Enter subject mark: 85
Enter attendance percentage: 85
Enter annual family income: 180000

Enter details of Student 3
Enter student name: Sita
Enter aggregate marks: 70
Enter number of subjects: 3
Enter subject mark: 75
Enter subject mark: 80
Enter subject mark: 70
Enter attendance percentage: 90
Enter annual family income: 150000
```

## 5. Sample Output

```
Sita is Not Eligible

===== SCHOLARSHIP ALLOCATION RESULTS =====

Rank  Name       Aggregate  Attendance  Income

1     Ravi       85         90          200000
2     Kumar      80         85          180000

Program Completed
```
