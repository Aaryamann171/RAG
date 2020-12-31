import random
import os
f = open("questionbank.txt", "r+")
student_name = input("Enter the student name: ")
student_rollnumber = input("Enter the student rollnumber: ")
os.system('touch {}.ms'.format(student_name))
ms_file = open("{}.ms".format(student_name), "w")
for line in f:
    questions = line.strip().split(',')
# print questions
unique_questions = list()
ms_data = ".PDFPIC /home/oreo/Documents/rnd_demo/rag/uni_logo.pdf 2\n.TL\nProgram: B. Tech. Discipline: CSE\n.AU\nSemester VI Academic Year 2020\n.AI\nEnd Semester Open book assignment\n.DA\n.B\nStudent Name: {}\nStudent Roll Number: {}\n.SH\n.nr instuction 1 1\nInstructions:\n.IP \\n[instuction] 3\nDon't copy from each other\n.IP \\n+[instuction]\nSubmit the exam before deadline\n.IP \\n+[instuction]\nAnswer all questions in your own words.\n.SH\nQuestions".format(
    student_name, student_rollnumber)

for i in range(5):
    unique_questions.append(questions.pop(random.randint(0, len(questions)-1)))
# print("NIIT UNIVERSITY")
# print("End Semeter")
for j in range(5):
    # print("Q{}. {}".format(j+1, unique_questions[j]))
    ms_data += ("\n.PP\nQ{}. {}".format(j+1, unique_questions[j]))

n = ms_file.write(ms_data)
ms_file.close()
os.system('groff -U -ms {}.ms -T pdf > {}.pdf'.format(student_name, student_name))
os.system('rm {}.ms'.format(student_name))
