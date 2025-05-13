# minimum average to pass
passing_grade = 7.0

# minimum average to take the final exam
exam_grade = 6.0

# number of terms in the year
terms = 4

# student's name
name = "Pedro Henrique"

# list of grades during the year - one per term
grades = [7.8, 8.5, 5.9, 8.1]

# message to be displayed at the end
message = ''

# loop to sum all yearly grades
total = 0
for grade in grades:
    total += grade

# calculate yearly average
average = total / terms

# decision structure to set the message
if average >= passing_grade:
    message = 'Approved'
elif average >= exam_grade:
    message = 'Final Exam'
else:
    message = 'Failed'

# Display results
print(f"Student: {name}")
print(f"Yearly average: {average:.1f}")
print(f"Status: {message}")