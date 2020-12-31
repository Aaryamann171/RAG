import random
import os

question_bank = open("questionbank.txt", "r+") # question bank in csv format
student_name = input("Enter the student name: ")
student_rollnumber = input("Enter the student rollnumber: ")

os.system('touch {}.ms'.format(student_name)) # creates a temporary ms file (will be deleted after program is finished)
ms_file = open("{}.ms".format(student_name), "w") # opening the ms file

# read questions from the question bank
for question in question_bank:
    questions = question.strip().split(',') # makes a list of all the questions

question_bank.close() # closing question bank file

# print(questions)

# enter your information here
logo = "uni_logo.pdf" # path to logo
program = "B.Tech."
discipline = "CSE"
semester = "VI"
academic_year = "2020-21"
exam_name = "End Semester Open Book Exam"
instructions = ("Don't copy from each other", "Submit the exam before deadline", "Answer all questions in your own words.")

ms_data = f".PDFPIC {logo} 2\n.TL\nProgram: {program} Discipline: {discipline}\n.AU\nSemester {semester} Academic Year {academic_year}\n.AI\n{exam_name}\n.DA\n.B\nStudent Name: {student_name}\nStudent Roll Number: {student_rollnumber}\n.SH\n.nr instuction 1 1\nInstructions:\n.IP \\n[instuction] 3\n{instructions[0]}\n.IP \\n+[instuction]\n{instructions[1]}\n.IP \\n+[instuction]\n{instructions[2]}\n.SH\nQuestions"


# adding 5 random questions to a new list called unique_questions
unique_questions = random.sample(questions, 5)

# print(unique_questions)

# adding the selected questions to the ms data string
for i in range(5):
    # print("Q{}. {}".format(i+1, unique_questions[i]))
    ms_data += ("\n.PP\nQ{}. {}".format(i+1, unique_questions[i]))

n = ms_file.write(ms_data) # wrting the ms data string to a ms file
ms_file.close() # closing ms file

os.system(f"groff -U -ms {student_name}.ms -T pdf > {student_name}.pdf") # coverts ms file to pdf
os.system(f"rm {student_name}.ms") # removes now redundant groff ms file
