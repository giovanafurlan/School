def calculate_grade (answer_, feed):
    grade = 0
    for x in range (len (feed)):
        if answer_ [x] == feed [x]:
            grade = grade + 1
    return grade

numQuestions = int (input ('Number of questions:'))
feedback = input ('Feedback:')
numStudents = int (input ('Number of students:'))

if numStudents > 100:
    print('Numer of studentes exceeded')

for i in range (numStudents):
    answer = input ('Student response:')
    grade = calculate_grade (answer, feedback)
    media = (grade / numQuestions)
    print('Grade:', media)

    if media > 7:
        print('Approved')
    else:
        print('Failed')
