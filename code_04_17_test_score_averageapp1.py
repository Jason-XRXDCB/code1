import streamlit as st
st.title("Jason's excellent score_averageapp")


# This program average test score. It asks the user for the number of students and the number of these score per student

# Initialize a list to store each student's average score
all_student_scores = []

# Get the number of students
num_student = int(st.number_input("How many students?: ", min_value = 1, step = 1, key ='num_students'))
# Get the number of test score per students
num_test_score = int(st.number_input("How many exams?: ", min_value = 1, step = 1, key ='num_exams'))

# Repeat task for students. Determine each students' average test score
for student in range(num_student):
    # Initialize an accumulator for test scores
    total = 0.0
    # Repeat calculation for exam
    st.write('Student number', student + 1)
    for test_num in range(num_test_score):
        # Add a print line for which number of exam you are
        st.write(f"Exam number {test_num + 1}")
        st.write("--------------")
        # Get a student's test score
        score = float(st.number_input(f"What is the score of exam {test_num + 1}?: ", key=f"score_{student}_{test_num}", min_value=0.0, max_value=100.0))
        # Add input validation for exam score. Each exam score should be in range of >= 0 to <= 100
        while score > 100 or score < 0:
            st.write("Error: the score can not exceed 100 or negative value")
            score = float(st.number_input(f"What is the score of exam {test_num + 1}?: ", key=f"score_{student}_{test_num}", min_value=0.0, max_value=100.0))
        total = score + total
    # Calculate the average test score for this students
    average = total / num_test_score
    # Display the average
    st.write(f'The average of the exams for student {student + 1} is {average}')
    # add calculation of average of all students
    all_student_scores.append(average)

if num_student > 0:
    # Calculate the overall average of all students' average scores
    overall_average = sum(all_student_scores) / len(all_student_scores)
    # Display the overall average
    st.write(f'The overall average of all students\' average scores is {overall_average}')
else:
    st.write("There are no students to calculate the overall average.")